/**
 * API Service for Coherence Backend
 */
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface Entry {
  id: string;
  content: string;
  type: string;
  tags: string[];
  created_at: string;
  updated_at: string;
  ai_categories: string[];
  ai_entities: any[];
  ai_summary?: string;
  ai_sentiment?: any;
  ai_key_phrases: string[];
  extracted_actions: any[];
  related_entry_ids: string[];
  view_count: number;
}

export interface CreateEntryRequest {
  content: string;
  type?: string;
  tags?: string[];
}

export interface SearchResult {
  entry: Entry;
  score: number;
  highlights: string[];
}

export interface GraphNode {
  id: string;
  label: string;
  type: string;
  size: number;
  metadata: any;
}

export interface GraphEdge {
  source: string;
  target: string;
  weight: number;
  type: string;
  label?: string;
}

export interface KnowledgeGraph {
  nodes: GraphNode[];
  edges: GraphEdge[];
  metadata: any;
}

// Entry API
export const entryAPI = {
  create: async (data: CreateEntryRequest): Promise<Entry> => {
    const response = await api.post('/api/v1/entries', data);
    return response.data;
  },

  list: async (params?: { limit?: number; offset?: number; type?: string; tag?: string }): Promise<Entry[]> => {
    const response = await api.get('/api/v1/entries', { params });
    return response.data;
  },

  get: async (id: string): Promise<Entry> => {
    const response = await api.get(`/api/v1/entries/${id}`);
    return response.data;
  },

  update: async (id: string, data: Partial<CreateEntryRequest>): Promise<Entry> => {
    const response = await api.put(`/api/v1/entries/${id}`, data);
    return response.data;
  },

  delete: async (id: string): Promise<void> => {
    await api.delete(`/api/v1/entries/${id}`);
  },
};

// Search API
export const searchAPI = {
  search: async (query: string, limit: number = 10): Promise<SearchResult[]> => {
    const response = await api.get('/api/v1/search', { params: { query, limit } });
    return response.data;
  },
};

// Graph API
export const graphAPI = {
  get: async (entryId?: string, depth: number = 2, minWeight: number = 0.5): Promise<KnowledgeGraph> => {
    const params = entryId
      ? { entry_id: entryId, depth, min_weight: minWeight }
      : { min_weight: minWeight };
    const response = await api.get('/api/v1/graph', { params });
    return response.data;
  },
};

// Stats API
export const statsAPI = {
  get: async (): Promise<any> => {
    const response = await api.get('/api/v1/stats');
    return response.data;
  },
};

export default api;
