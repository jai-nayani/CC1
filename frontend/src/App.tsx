import { useEffect } from 'react';
import { useStore } from './store/useStore';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import CaptureView from './pages/CaptureView';
import TimelineView from './pages/TimelineView';
import GraphView from './pages/GraphView';
import SearchView from './pages/SearchView';

function App() {
  const { currentView, darkMode, sidebarOpen } = useStore();

  useEffect(() => {
    // Initialize dark mode
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  const renderView = () => {
    switch (currentView) {
      case 'capture':
        return <CaptureView />;
      case 'timeline':
        return <TimelineView />;
      case 'graph':
        return <GraphView />;
      case 'search':
        return <SearchView />;
      default:
        return <TimelineView />;
    }
  };

  return (
    <div className="flex h-screen overflow-hidden bg-gray-50 dark:bg-gray-900">
      {sidebarOpen && <Sidebar />}

      <div className="flex flex-col flex-1 overflow-hidden">
        <Header />

        <main className="flex-1 overflow-y-auto p-6">
          <div className="max-w-7xl mx-auto">
            {renderView()}
          </div>
        </main>
      </div>
    </div>
  );
}

export default App;
