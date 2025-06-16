'use client';

import { useFeatureFlag } from '@/lib/feature-flags';

export default function CustomAgentFlagPage() {
  const { enabled, loading, error } = useFeatureFlag('custom_agent');

  return (
    <div className="max-w-md mx-auto my-12 p-4 border rounded">
      <h1 className="text-2xl font-bold mb-4">Custom Agent Feature Flag</h1>
      {loading && <p>Loading flag status...</p>}
      {error && <p className="text-red-500">Error: {error}</p>}
      {!loading && !error && (
        <p>
          The <code>custom_agent</code> flag is{' '}
          <span className={enabled ? 'text-green-600' : 'text-red-600'}>
            {enabled ? 'ENABLED' : 'DISABLED'}
          </span>
          .
        </p>
      )}
    </div>
  );
}
