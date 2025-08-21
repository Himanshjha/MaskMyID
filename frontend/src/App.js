import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import ResultView from "./components/ResultView";

function App() {
  const [maskedImage, setMaskedImage] = useState(null);
  const [details, setDetails] = useState(null);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 text-center p-6">
  {/* Heading */}
  <h1 className="text-5xl font-extrabold text-white drop-shadow-md mb-2">
    MaskMyID 🔒
  </h1>
  <p className="text-xl text-white/90 mb-10">
    Protect your personal information
  </p>
  {/* Card Container - balanced width and content centering */}
  <div className="bg-white/30 backdrop-blur-lg shadow-2xl rounded-3xl p-10 w-full max-w-md flex flex-col items-center gap-8 border border-white/40 mx-auto">
    <UploadForm onResult={setMaskedImage} onDetails={setDetails} />
    <ResultView maskedImage={maskedImage} details={details} />
  </div>
  {/* Footer */}
  <footer className="mt-10 text-white/95 font-medium text-lg">
    Built with ❤️ by Himanshu Jha 🚀
  </footer>
</div>

  );
}

export default App;

