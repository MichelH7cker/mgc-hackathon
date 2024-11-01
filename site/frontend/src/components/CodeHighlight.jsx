import React, { useEffect } from 'react';
import Prism from 'prismjs';

const CodeHighlight = ({ codeString, language }) => {
  useEffect(() => {
    Prism.highlightAll();
  }, [codeString]);

  return (
    <pre className="bg-gray-800 p-4 rounded-lg overflow-auto">
      <code className={`language-${language}`}>
        {codeString}
      </code>
    </pre>
  );
};
export default CodeHighlight;
