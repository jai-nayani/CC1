import { useState } from 'react';
import { searchAPI, SearchResult } from '../services/api';
import { formatDistanceToNow } from 'date-fns';

export default function SearchView() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isSearching, setIsSearching] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!query.trim()) return;

    setIsSearching(true);
    setHasSearched(true);

    try {
      const data = await searchAPI.search(query.trim());
      setResults(data);
    } catch (error) {
      console.error('Error searching:', error);
    } finally {
      setIsSearching(false);
    }
  };

  return (
    <div className="animate-fade-in max-w-4xl mx-auto">
      <div className="mb-8">
        <h2 className="text-3xl font-bold mb-2">Semantic Search</h2>
        <p className="text-gray-600 dark:text-gray-400">
          Find entries by meaning, not just keywords. AI understands context.
        </p>
      </div>

      <form onSubmit={handleSearch} className="mb-8">
        <div className="card">
          <div className="flex gap-3">
            <div className="flex-1 relative">
              <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Search anything... e.g., 'ideas about AI', 'meetings last week', 'tasks for tomorrow'"
                className="w-full pl-12 pr-4 py-4 bg-transparent border-none outline-none text-lg"
                disabled={isSearching}
              />
              <svg
                className="absolute left-4 top-1/2 -translate-y-1/2 w-6 h-6 text-gray-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>

            <button
              type="submit"
              disabled={isSearching || !query.trim()}
              className="btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isSearching ? (
                <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
              ) : (
                'Search'
              )}
            </button>
          </div>
        </div>
      </form>

      {isSearching && (
        <div className="text-center py-12">
          <div className="w-12 h-12 border-4 border-primary-600 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-gray-600 dark:text-gray-400">Searching through your knowledge...</p>
        </div>
      )}

      {!isSearching && hasSearched && (
        <div className="mb-6">
          <p className="text-sm text-gray-600 dark:text-gray-400">
            Found {results.length} {results.length === 1 ? 'result' : 'results'} for "{query}"
          </p>
        </div>
      )}

      {!isSearching && results.length > 0 && (
        <div className="space-y-4">
          {results.map((result) => (
            <SearchResultCard key={result.entry.id} result={result} />
          ))}
        </div>
      )}

      {!isSearching && hasSearched && results.length === 0 && (
        <div className="card text-center py-16">
          <svg className="w-16 h-16 mx-auto mb-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <h3 className="text-xl font-semibold mb-2">No results found</h3>
          <p className="text-gray-600 dark:text-gray-400">
            Try different keywords or create a new entry
          </p>
        </div>
      )}

      {!hasSearched && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="card">
            <h3 className="font-semibold mb-3">Search Examples</h3>
            <div className="space-y-2">
              {[
                'ideas about startups',
                'meetings with investors',
                'tasks due this week',
                'notes about AI',
                'decisions made last month',
              ].map((example) => (
                <button
                  key={example}
                  onClick={() => setQuery(example)}
                  className="w-full text-left px-3 py-2 bg-gray-50 dark:bg-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 rounded-lg text-sm transition-colors"
                >
                  "{example}"
                </button>
              ))}
            </div>
          </div>

          <div className="card">
            <h3 className="font-semibold mb-3">How It Works</h3>
            <div className="space-y-3 text-sm text-gray-600 dark:text-gray-400">
              <div className="flex gap-3">
                <svg className="w-5 h-5 text-primary-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <p>Searches by meaning, not just exact words</p>
              </div>
              <div className="flex gap-3">
                <svg className="w-5 h-5 text-primary-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <p>Understands context and relationships</p>
              </div>
              <div className="flex gap-3">
                <svg className="w-5 h-5 text-primary-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <p>Ranks results by relevance</p>
              </div>
              <div className="flex gap-3">
                <svg className="w-5 h-5 text-primary-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <p>Learns from your usage patterns</p>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

function SearchResultCard({ result }: { result: SearchResult }) {
  const { entry, score } = result;
  const [isExpanded, setIsExpanded] = useState(false);

  const getTypeColor = (type: string) => {
    const colors: Record<string, string> = {
      note: 'bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-400',
      task: 'bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-400',
      idea: 'bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-400',
      meeting: 'bg-orange-100 dark:bg-orange-900/30 text-orange-700 dark:text-orange-400',
    };
    return colors[type] || colors.note;
  };

  const relevancePercentage = Math.round(score * 100);

  return (
    <div className="card hover:shadow-lg transition-shadow border-l-4 border-primary-500">
      <div className="flex items-start justify-between mb-3">
        <div className="flex items-center gap-3 flex-wrap">
          <span className={`px-3 py-1 rounded-full text-xs font-medium ${getTypeColor(entry.type)}`}>
            {entry.type}
          </span>
          <span className="text-xs px-2 py-1 bg-primary-100 dark:bg-primary-900/30 text-primary-700 dark:text-primary-400 rounded-full font-medium">
            {relevancePercentage}% match
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
        <div className="flex flex-wrap gap-2">
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
    </div>
  );
}
