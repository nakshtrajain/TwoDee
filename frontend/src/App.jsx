import React, { useState } from 'react';
import PromptInput from './components/PromptInput';
import VideoDisplay from './components/VideoDisplay';

function App() {
  const [videoUrl, setVideoUrl] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleVideoGenerated = (url) => {
    setVideoUrl(url);
    setLoading(false);
    setError(null);
  };

  const handleError = (errorMessage) => {
    setError(errorMessage);
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <header className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">TwoDee Animation Generator</h1>
          <p className="text-lg text-gray-600">Create beautiful 2D animations from text prompts</p>
        </header>

        <div className="max-w-3xl mx-auto">
          <PromptInput 
            onSubmit={() => setLoading(true)}
            onVideoGenerated={handleVideoGenerated}
            onError={handleError}
          />

          {error && (
            <div className="mt-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded">
              {error}
            </div>
          )}

          {loading && (
            <div className="mt-8 text-center">
              <div className="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-blue-500"></div>
              <p className="mt-2 text-gray-600">Generating your animation...</p>
            </div>
          )}

          {videoUrl && !loading && (
            <div className="mt-8">
              <VideoDisplay videoUrl={videoUrl} />
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App; 