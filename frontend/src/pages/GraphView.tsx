import { useEffect, useState } from 'react';
import { useStore } from '../store/useStore';
import { graphAPI } from '../services/api';

export default function GraphView() {
  const { graph, setGraph, graphLoading, setGraphLoading } = useStore();
  const [depth, setDepth] = useState(2);
  const [minWeight, setMinWeight] = useState(0.5);

  useEffect(() => {
    loadGraph();
  }, [depth, minWeight]);

  const loadGraph = async () => {
    setGraphLoading(true);
    try {
      const data = await graphAPI.get(undefined, depth, minWeight);
      setGraph(data);
    } catch (error) {
      console.error('Error loading graph:', error);
    } finally {
      setGraphLoading(false);
    }
  };

  if (graphLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-center">
          <div className="w-12 h-12 border-4 border-primary-600 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-gray-600 dark:text-gray-400">Building knowledge graph...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="animate-fade-in">
      <div className="mb-8">
        <h2 className="text-3xl font-bold mb-2">Knowledge Graph</h2>
        <p className="text-gray-600 dark:text-gray-400">
          Visualize how your ideas and notes connect
        </p>
      </div>

      <div className="card mb-6">
        <div className="flex items-center gap-6">
          <div className="flex-1">
            <label className="block text-sm font-medium mb-2">Connection Depth</label>
            <input
              type="range"
              min="1"
              max="3"
              value={depth}
              onChange={(e) => setDepth(Number(e.target.value))}
              className="w-full"
            />
            <div className="flex justify-between text-xs text-gray-500 mt-1">
              <span>1 level</span>
              <span>2 levels</span>
              <span>3 levels</span>
            </div>
          </div>

          <div className="flex-1">
            <label className="block text-sm font-medium mb-2">Minimum Similarity</label>
            <input
              type="range"
              min="0"
              max="1"
              step="0.1"
              value={minWeight}
              onChange={(e) => setMinWeight(Number(e.target.value))}
              className="w-full"
            />
            <div className="flex justify-between text-xs text-gray-500 mt-1">
              <span>0% (All)</span>
              <span>50%</span>
              <span>100% (Strong)</span>
            </div>
          </div>
        </div>
      </div>

      {graph && graph.nodes.length > 0 ? (
        <div className="card">
          <div className="mb-6">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-6">
                <div>
                  <div className="text-3xl font-bold text-primary-600">{graph.nodes.length}</div>
                  <div className="text-sm text-gray-600 dark:text-gray-400">Nodes</div>
                </div>
                <div>
                  <div className="text-3xl font-bold text-primary-600">{graph.edges.length}</div>
                  <div className="text-sm text-gray-600 dark:text-gray-400">Connections</div>
                </div>
              </div>
            </div>

            <div className="h-96 bg-gray-100 dark:bg-gray-900 rounded-lg flex items-center justify-center border-2 border-dashed border-gray-300 dark:border-gray-700">
              <div className="text-center">
                <svg className="w-16 h-16 mx-auto mb-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
                </svg>
                <p className="text-gray-600 dark:text-gray-400">
                  Interactive graph visualization
                </p>
                <p className="text-sm text-gray-500 mt-2">
                  Graph data loaded • {graph.nodes.length} nodes, {graph.edges.length} edges
                </p>
                <p className="text-xs text-gray-400 mt-4">
                  (Full D3.js/React Flow visualization would be rendered here)
                </p>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
            <div>
              <h3 className="font-semibold mb-3">Top Nodes</h3>
              <div className="space-y-2">
                {graph.nodes.slice(0, 5).map((node) => (
                  <div key={node.id} className="p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
                    <div className="font-medium text-sm truncate">{node.label}</div>
                    <div className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                      {node.type} • Size: {node.size}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div>
              <h3 className="font-semibold mb-3">Connection Types</h3>
              <div className="space-y-2">
                {Array.from(new Set(graph.edges.map(e => e.type))).map((type) => {
                  const count = graph.edges.filter(e => e.type === type).length;
                  return (
                    <div key={type} className="p-3 bg-gray-50 dark:bg-gray-700 rounded-lg flex items-center justify-between">
                      <span className="font-medium text-sm capitalize">{type}</span>
                      <span className="text-xs px-2 py-1 bg-primary-100 dark:bg-primary-900/30 text-primary-700 dark:text-primary-400 rounded-full">
                        {count}
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      ) : (
        <div className="card text-center py-16">
          <svg className="w-16 h-16 mx-auto mb-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
          </svg>
          <h3 className="text-xl font-semibold mb-2">No connections yet</h3>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            Create more entries to see how your knowledge connects!
          </p>
        </div>
      )}
    </div>
  );
}
