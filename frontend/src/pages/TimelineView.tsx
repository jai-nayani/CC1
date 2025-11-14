import { useEffect, useState } from 'react';
import { useStore } from '../store/useStore';
import { entryAPI, Entry } from '../services/api';
import { formatDistanceToNow } from 'date-fns';

export default function TimelineView() {
  const { entries, setEntries, isLoading, setLoading, setCurrentView } = useStore();
  const [selectedFilter, setSelectedFilter] = useState<string>('all');

  useEffect(() => {
    loadEntries();
  }, []);

  const loadEntries = async () => {
    setLoading(true);
    try {
      const data = await entryAPI.list({ limit: 50 });
      setEntries(data);
    } catch (error) {
      console.error('Error loading entries:', error);
    } finally {
      setLoading(false);
    }
  };

  const getTypeColor = (type: string) => {
    const colors: Record<string, string> = {
      note: 'bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400',
      task: 'bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-400',
      idea: 'bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-400',
      meeting: 'bg-orange-100 dark:bg-orange-900/30 text-orange-700 dark:text-orange-400',
      reference: 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-400',
    };
    return colors[type] || colors.note;
  };

  const filteredEntries = selectedFilter === 'all'
    ? entries
    : entries.filter(e => e.type === selectedFilter);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-center">
          <div className="w-12 h-12 border-4 border-primary-600 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-gray-600 dark:text-gray-400">Loading your entries...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="animate-fade-in">
      <div className="mb-8 flex items-center justify-between">
        <div>
          <h2 className="text-3xl font-bold mb-2">Timeline</h2>
          <p className="text-gray-600 dark:text-gray-400">
            {filteredEntries.length} entries • Sorted by most recent
          </p>
        </div>

        <button
          onClick={() => setCurrentView('capture')}
          className="btn-primary flex items-center gap-2"
        >
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
          </svg>
          <span>New Entry</span>
        </button>
      </div>

      <div className="flex gap-2 mb-6 overflow-x-auto pb-2">
        {['all', 'note', 'task', 'idea', 'meeting', 'reference'].map((filter) => (
          <button
            key={filter}
            onClick={() => setSelectedFilter(filter)}
            className={`
              px-4 py-2 rounded-lg font-medium transition-all whitespace-nowrap
              ${selectedFilter === filter
                ? 'bg-primary-600 text-white shadow-md'
                : 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
              }
            `}
          >
            {filter.charAt(0).toUpperCase() + filter.slice(1)}
          </button>
        ))}
      </div>

      {filteredEntries.length === 0 ? (
        <div className="card text-center py-16">
          <svg className="w-16 h-16 mx-auto mb-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <h3 className="text-xl font-semibold mb-2">No entries yet</h3>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            Start by capturing your first thought, idea, or note!
          </p>
          <button
            onClick={() => setCurrentView('capture')}
            className="btn-primary"
          >
            Create First Entry
          </button>
        </div>
      ) : (
        <div className="space-y-4">
          {filteredEntries.map((entry) => (
            <EntryCard key={entry.id} entry={entry} getTypeColor={getTypeColor} />
          ))}
        </div>
      )}
    </div>
  );
}

function EntryCard({ entry, getTypeColor }: { entry: Entry; getTypeColor: (type: string) => string }) {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div className="card hover:shadow-lg transition-shadow">
      <div className="flex items-start justify-between mb-3">
        <div className="flex items-center gap-2">
          <span className={`px-3 py-1 rounded-full text-xs font-medium ${getTypeColor(entry.type)}`}>
            {entry.type}
          </span>
          <span className="text-xs text-gray-500 dark:text-gray-400">
            {formatDistanceToNow(new Date(entry.created_at), { addSuffix: true })}
          </span>
        </div>

        <button
          onClick={() => setIsExpanded(!isExpanded)}
          className="p-1 hover:bg-gray-100 dark:hover:bg-gray-700 rounded transition-colors"
        >
          <svg
            className={`w-5 h-5 transition-transform ${isExpanded ? 'rotate-180' : ''}`}
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </button>
      </div>

      <p className="text-gray-800 dark:text-gray-200 mb-3 whitespace-pre-wrap">
        {isExpanded ? entry.content : entry.content.slice(0, 200) + (entry.content.length > 200 ? '...' : '')}
      </p>

      {entry.ai_categories && entry.ai_categories.length > 0 && (
        <div className="flex flex-wrap gap-2 mb-3">
          {entry.ai_categories.map((category, idx) => (
            <span
              key={idx}
              className="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded text-xs"
            >
              #{category}
            </span>
          ))}
        </div>
      )}

      {isExpanded && entry.ai_summary && (
        <div className="mt-4 p-3 bg-primary-50 dark:bg-primary-900/10 rounded-lg border-l-4 border-primary-500">
          <p className="text-sm text-gray-700 dark:text-gray-300">
            <strong className="text-primary-600 dark:text-primary-400">AI Summary:</strong> {entry.ai_summary}
          </p>
        </div>
      )}

      {isExpanded && entry.ai_key_phrases && entry.ai_key_phrases.length > 0 && (
        <div className="mt-3">
          <p className="text-xs font-medium text-gray-500 dark:text-gray-400 mb-2">Key Phrases:</p>
          <div className="flex flex-wrap gap-2">
            {entry.ai_key_phrases.map((phrase, idx) => (
              <span
                key={idx}
                className="px-2 py-1 bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-400 rounded text-xs"
              >
                {phrase}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
