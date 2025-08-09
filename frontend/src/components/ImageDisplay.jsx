import React from 'react';

function ImageDisplay({ imageUrl, prompt }) {
  return (
    <div className="bg-white rounded-lg shadow-lg overflow-hidden">
      <div className="p-4 border-b">
        <h3 className="text-lg font-semibold text-gray-800">Generated Drawing</h3>
        <p className="text-sm text-gray-600 mt-1">Prompt: "{prompt}"</p>
      </div>
      <div className="p-4">
        <div className="relative">
          <img
            src={imageUrl}
            alt="Generated turtle drawing"
            className="w-full h-auto max-w-full rounded-lg shadow-sm border"
            style={{ maxHeight: '600px', objectFit: 'contain' }}
          />
        </div>
      </div>
      <div className="p-4 bg-gray-50 border-t">
        <p className="text-xs text-gray-500">
          Drawing generated using Python Turtle Graphics
        </p>
      </div>
    </div>
  );
}

export default ImageDisplay;
