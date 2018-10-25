import java.util.*;

/*
 * Most complicated UVA-assignment of them all...
 *
 * 1. Read in the mazes from stdio and place each character in a matrix
 * 2. Create a graph containing nodes for all whitespace, A:s and S.
 * 3. Add edges between adjacent neighbors without weight (or rather w = 1)
 * 4. Replace all whitespace nodes with a weight cost of 1 to determine
 *    costs to move between A:s and S. To do this perform a BFS from
 *    each A and S in the maze. Add together spawned edges into a single graph.
 * 5. Calculate a MST using Kruskal's algorithm. The min-cost will be the lowest cost
 *    for traversing the MST. To use Kruskal's algorithm sort all edges by weight
 *    and then use a disjointed set data-structure to prevent redundant edges.
 */

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int testCases = Integer.parseInt(scanner.nextLine());

		for (int i = 0; i < testCases; ++i) {
			String[] dimensions = scanner.nextLine().split(" ");
			int rows = Integer.parseInt(dimensions[1]),
				cols = Integer.parseInt(dimensions[0]);

			char[][] maze = new char[rows][cols];

			StringBuilder mazePart = new StringBuilder();
			for (int j = 0; j < rows; ++j) {
				int length = mazePart.length();

				mazePart.append(scanner.nextLine());
				for (int k = 0; k < mazePart.length() - length; ++k) {
					maze[j][k] = mazePart.charAt(length + k);
				}
			}

			Graph g = Main.getGraphFromMaze(maze);
			g.rows = rows;
			g.cols = cols;
			g.setWeights();
			System.out.println(g.getLowestCost());
		}

		scanner.close();
	}

	public static Graph getGraphFromMaze(char[][] maze) {
		HashMap<String, ArrayList<Edge>> vertices = new HashMap<>();
		HashMap<String, Character>   vertexValues = new HashMap<>();

		for (int i = 0; i < maze.length; ++i) {
			for (int j = 0; j < maze[i].length; ++j) {
				/* Do not add maze borders or null signs */
				if (maze[i][j] != '#' && maze[i][j] != '\u0000') {
					ArrayList<Edge> edges = new ArrayList<>();
					vertexValues.put("" + i + "," + j, maze[i][j]);

					if (j - 1 > 0) {
						if (maze[i][j - 1] != '#' && maze[i][j - 1] != '\u0000') {
							edges.add(new Edge("" + i + "," + j, "" + i + "," + (j - 1)));
						}
					}

					if (i - 1 > 0) {
						if (maze[i - 1][j] != '#' && maze[i - 1][j] != '\u0000') {
							edges.add(new Edge("" + i + "," + j, "" + (i - 1) + "," + j));
						}
					}

					if (j + 1 < maze[i].length) {
						if (maze[i][j + 1] != '#' && maze[i][j + 1] != '\u0000') {
							edges.add(new Edge("" + i + "," + j, "" + i + "," + (j + 1)));
						}
					}

					if (i + 1 < maze.length) {
						if (maze[i + 1][j] != '#' && maze[i + 1][j] != '\u0000') {
							edges.add(new Edge("" + i + "," + j, "" + (i + 1) + "," + j));
						}
					}

					vertices.put("" + i + "," + j, edges);
				}
			}
		}

		Graph g = new Graph(vertices);
		g.vertexValues = vertexValues;

		return g;
	}
}

class Graph {
	HashMap<String, ArrayList<Edge>> vertices;
	HashMap<String, Character> vertexValues;
	ArrayList<Edge> allEdges;
	int rows, cols;

	public Graph(HashMap<String, ArrayList<Edge>> vertices) {
		this.vertices = vertices;
		allEdges = new ArrayList<>();
	}

	public void setWeights() {
		HashMap<String, ArrayList<Edge>> updatedGraph = new HashMap<>();

		for (String vertex: vertices.keySet()) {
			if (vertexValues.get(vertex) != ' ') {
				ArrayList<Edge> updatedEdges = bfs(vertex);
				updatedGraph.put(vertex, updatedEdges);
			}
		}

		vertices = updatedGraph;
	}

	public ArrayList<Edge> bfs(String root) {
		Queue<String> vertexQueue = new LinkedList<>();
		boolean[][] visited = new boolean[rows][cols];
		String[] dimensions = root.split(",");
		int rootRows = Integer.parseInt(dimensions[0]),
			rootCols = Integer.parseInt(dimensions[1]);

		visited[rootRows][rootCols] = true;
		vertexQueue.add(root);

		ArrayList<Edge> updatedEdges = new ArrayList<>();
		HashMap<String, Integer> vertexDistance = new HashMap<>();
		vertexDistance.put(root, 1);

		while(!vertexQueue.isEmpty()) {
			String curent = vertexQueue.remove();
			ArrayList<Edge> edges = vertices.get(curent);

			for (Edge edge: edges) {
				String vertex = edge.vertexTo;
				String[] vertexPosition = vertex.split(",");
				int vertexRow = Integer.parseInt(vertexPosition[0]),
					vertexCol = Integer.parseInt(vertexPosition[1]);

				if (!visited[vertexRow][vertexCol]) {
					visited[vertexRow][vertexCol] = true;
					vertexDistance.put(vertex, vertexDistance.get(curent) + 1);

					if (vertexValues.get(vertex) != ' ') {
						Edge updatedEdge = new Edge(root, vertex);
						updatedEdge.weight = vertexDistance.get(curent);
						updatedEdges.add(updatedEdge);
						allEdges.add(updatedEdge);
					}

					vertexQueue.add(vertex);
				}
			}
		}

		return updatedEdges;
	}

	public int getLowestCost() {
		DisjoinedSet ds = new DisjoinedSet(vertices);
		int totalWeight = 0;

		allEdges.sort(new CompareByWeight());

		for (Edge edge: allEdges) {
			String firstParent = ds.find(edge.vertexFrom);
			String secondParent = ds.find(edge.vertexTo);
			if (!firstParent.equals(secondParent)) {
				totalWeight += edge.weight;
				ds.union(firstParent, secondParent);
			}
		}

		return totalWeight;
	}

	private class CompareByWeight implements Comparator<Edge> {
		public int compare(Edge e1, Edge e2) {
			if (e1.weight > e2.weight) {
				return 1;
			}
			else if (e1.weight < e2.weight) {
				return -1;
			}

			return 0;
		}
	}
}

class Edge {
	int     weight;
	String  vertexFrom,
			vertexTo;

	public Edge(String vertexFrom, String vertexTo) {
		this.vertexFrom = vertexFrom;
		this.vertexTo = vertexTo;
	}
}

class DisjoinedSet {
	private HashMap<String, String> parents;
	private HashMap<String, Integer> ranks;

	public DisjoinedSet(HashMap<String, ArrayList<Edge>> vertices) {
		parents = new HashMap<>();
		ranks   = new HashMap<>();

		for (String vertex: vertices.keySet()) {
			parents.put(vertex, vertex);
			ranks.put(vertex, 0);
		}
	}

	public String find(String vertex) {
		if (parents.get(vertex).equals(vertex)) {
			return vertex;
		}

		return find(parents.get(vertex));
	}

	public void union(String firstSet, String secondSet) {
		if (ranks.get(firstSet) > ranks.get(secondSet)) {
			parents.put(secondSet, firstSet);
		}
		else if (ranks.get(secondSet) > ranks.get(firstSet)) {
			parents.put(firstSet, secondSet);
		}
		else {
			parents.put(firstSet, secondSet);
			ranks.put(secondSet, ranks.get(secondSet) + 1);
		}
	}
}


