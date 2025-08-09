import React, { useState } from 'react';
import { generateDrawing } from '../api';

function PromptInput({ onSubmit, onDrawingGenerated, onError }) {
  const [prompt, setPrompt] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!prompt.trim()) return;

    try {
      onSubmit(prompt);
      const response = await generateDrawing(prompt);
      
      if (response.status === 'success') {
        onDrawingGenerated(`http://localhost:8000${response.image_url}`, prompt);
      } else {
        onError(response.message || 'Failed to generate drawing');
      }
    } catch (error) {
      onError(error.response?.data?.message || error.message || 'Failed to generate drawing');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label 
          htmlFor="prompt" 
          className="block text-sm font-medium text-gray-700 mb-2"
        >
          Enter your drawing prompt
        </label>
        <textarea
          id="prompt"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          className="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
          placeholder="Example: draw a red circle, draw a blue house, draw a filled green star"
          rows="3"
        />
      </div>
      <button
        type="submit"
        className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
        disabled={!prompt.trim()}
      >
        Generate Drawing
      </button>
    </form>
  );
}

export default PromptInput; 