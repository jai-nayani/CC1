import { useState } from 'react';
import { useStore } from '../store/useStore';
import { entryAPI, CreateEntryRequest } from '../services/api';

export default function CaptureView() {
  const [content, setContent] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [successMessage, setSuccessMessage] = useState('');
  const { addEntry } = useStore();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!content.trim()) return;

    setIsSubmitting(true);
    setSuccessMessage('');

    try {
      const data: CreateEntryRequest = {
        content: content.trim(),
        type: 'note',
        tags: [],
      };

      const newEntry = await entryAPI.create(data);
      addEntry(newEntry);

      setContent('');
      setSuccessMessage('✨ Entry captured! AI is processing your content...');

      setTimeout(() => setSuccessMessage(''), 3000);
    } catch (error) {
      console.error('Error creating entry:', error);
      alert('Failed to create entry. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto animate-fade-in">
      <div className="mb-8">
        <h2 className="text-3xl font-bold mb-2">Capture Your Thoughts</h2>
        <p className="text-gray-600 dark:text-gray-400">
          Write anything. AI will automatically organize, extract actions, and build connections.
        </p>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="card">
          <textarea
            value={content}
            onChange={(e) => setContent(e.target.value)}
            placeholder="What's on your mind? Write a note, idea, task, or anything else...

Examples:
• Meeting with Sarah tomorrow at 2pm to discuss Q4 roadmap
• Idea: AI-powered personal assistant that learns from your habits
• Need to finish the presentation by Friday
• Just learned about knowledge graphs - fascinating!"
            className="w-full min-h-[400px] p-4 bg-transparent border-none outline-none resize-none text-lg"
            disabled={isSubmitting}
          />
        </div>

        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
              <span>AI will analyze and organize</span>
            </div>
          </div>

          <button
            type="submit"
            disabled={isSubmitting || !content.trim()}
            className="btn-primary disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
          >
            {isSubmitting ? (
              <>
                <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                <span>Processing...</span>
              </>
            ) : (
              <>
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
                <span>Capture</span>
              </>
            )}
          </button>
        </div>

        {successMessage && (
          <div className="p-4 bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-400 rounded-lg animate-slide-up">
            {successMessage}
          </div>
        )}
      </form>

      <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="card">
          <div className="w-10 h-10 bg-primary-100 dark:bg-primary-900/30 rounded-lg flex items-center justify-center mb-3">
            <svg className="w-6 h-6 text-primary-600 dark:text-primary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
          <h3 className="font-semibold mb-1">Auto-Organization</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            AI automatically categorizes and tags your entries
          </p>
        </div>

        <div className="card">
          <div className="w-10 h-10 bg-primary-100 dark:bg-primary-900/30 rounded-lg flex items-center justify-center mb-3">
            <svg className="w-6 h-6 text-primary-600 dark:text-primary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <h3 className="font-semibold mb-1">Action Extraction</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            Tasks and deadlines are automatically detected
          </p>
        </div>

        <div className="card">
          <div className="w-10 h-10 bg-primary-100 dark:bg-primary-900/30 rounded-lg flex items-center justify-center mb-3">
            <svg className="w-6 h-6 text-primary-600 dark:text-primary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
            </svg>
          </div>
          <h3 className="font-semibold mb-1">Smart Connections</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            Related ideas are automatically linked together
          </p>
        </div>
      </div>
    </div>
  );
}
