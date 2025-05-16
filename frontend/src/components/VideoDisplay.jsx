import React from 'react';
import ReactPlayer from 'react-player';

function VideoDisplay({ videoUrl }) {
  return (
    <div className="aspect-w-16 aspect-h-9 bg-black rounded-lg overflow-hidden">
      <ReactPlayer
        url={videoUrl}
        width="100%"
        height="100%"
        controls={true}
        playing={true}
        config={{
          file: {
            attributes: {
              controlsList: 'nodownload',
            },
          },
        }}
      />
    </div>
  );
}

export default VideoDisplay; 