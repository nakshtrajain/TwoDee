import React, { useState } from 'react';
import { generateVideo } from '../api';

function PromptInput({ onSubmit, onVideoGenerated, onError }) {
  const [prompt, setPrompt] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!prompt.trim()) return;

    try {
      onSubmit();
      const response = await generateVideo(prompt);
      onVideoGenerated(`http://localhost:8000${response.video_url}`);
    } catch (error) {
      onError(error.response?.data?.detail || 'Failed to generate video');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label 
          htmlFor="prompt" 
          className="block text-sm font-medium text-gray-700 mb-2"
        >
          Enter your animation prompt
        </label>
        <textarea
          id="prompt"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          className="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          placeholder="Example: Create a circle that transforms into a square"
          rows="3"
        />
      </div>
      <button
        type="submit"
        className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
        disabled={!prompt.trim()}
      >
        Generate Animation
      </button>
    </form>
  );
}

export default PromptInput; 