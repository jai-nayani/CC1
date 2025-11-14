/**
 * Global state management with Zustand
 */
import { create } from 'zustand';
import { Entry, KnowledgeGraph } from '../services/api';

interface CoherenceState {
  // Entries
  entries: Entry[];
  selectedEntry: Entry | null;
  isLoading: boolean;
  error: string | null;

  // Graph
  graph: KnowledgeGraph | null;
  graphLoading: boolean;

  // UI State
  darkMode: boolean;
  sidebarOpen: boolean;
  currentView: 'timeline' | 'graph' | 'search' | 'capture';

  // Actions
  setEntries: (entries: Entry[]) => void;
  addEntry: (entry: Entry) => void;
  updateEntry: (id: string, updates: Partial<Entry>) => void;
  deleteEntry: (id: string) => void;
  setSelectedEntry: (entry: Entry | null) => void;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;

  setGraph: (graph: KnowledgeGraph | null) => void;
  setGraphLoading: (loading: boolean) => void;

  toggleDarkMode: () => void;
  toggleSidebar: () => void;
  setCurrentView: (view: 'timeline' | 'graph' | 'search' | 'capture') => void;
}

export const useStore = create<CoherenceState>((set) => ({
  // Initial state
  entries: [],
  selectedEntry: null,
  isLoading: false,
  error: null,

  graph: null,
  graphLoading: false,

  darkMode: window.matchMedia('(prefers-color-scheme: dark)').matches,
  sidebarOpen: true,
  currentView: 'timeline',

  // Actions
  setEntries: (entries) => set({ entries }),

  addEntry: (entry) =>
    set((state) => ({
      entries: [entry, ...state.entries],
    })),

  updateEntry: (id, updates) =>
    set((state) => ({
      entries: state.entries.map((entry) =>
        entry.id === id ? { ...entry, ...updates } : entry
      ),
      selectedEntry:
        state.selectedEntry?.id === id
          ? { ...state.selectedEntry, ...updates }
          : state.selectedEntry,
    })),

  deleteEntry: (id) =>
    set((state) => ({
      entries: state.entries.filter((entry) => entry.id !== id),
      selectedEntry: state.selectedEntry?.id === id ? null : state.selectedEntry,
    })),

  setSelectedEntry: (entry) => set({ selectedEntry: entry }),

  setLoading: (loading) => set({ isLoading: loading }),

  setError: (error) => set({ error }),

  setGraph: (graph) => set({ graph }),

  setGraphLoading: (loading) => set({ graphLoading: loading }),

  toggleDarkMode: () =>
    set((state) => {
      const newDarkMode = !state.darkMode;
      if (newDarkMode) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
      return { darkMode: newDarkMode };
    }),

  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),

  setCurrentView: (view) => set({ currentView: view }),
}));
