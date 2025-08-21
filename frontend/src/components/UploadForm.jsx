import React, { useState } from "react";

function UploadForm({ onResult, onDetails }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please select an image first!");

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      // Get masked image
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      onResult(url);

      // Optional: If backend also sends detected PII JSON
      // const data = await res.json();
      // onDetails(data);
    } catch (err) {
      console.error(err);
      alert("Upload failed!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full max-w-md p-8 bg-white/30 backdrop-blur-lg shadow-2xl rounded-3xl border border-gray-200 flex flex-col items-center">
      <h2 className="text-3xl font-bold text-indigo-700 mb-2">
        MaskMyID 🔒
      </h2>
      <p className="text-gray-700 text-sm mb-6">
        Secure your ID in seconds
      </p>

      <label className="w-full cursor-pointer mb-6">
        <div className="flex flex-col items-center justify-center border-2 border-dashed border-indigo-300 rounded-xl p-6 bg-white/40 hover:bg-white/60 transition">
          <span className="text-indigo-600 font-medium">📂 Choose File</span>
          <span className="text-xs text-gray-500 mt-1">
            {file ? file.name : "No file chosen"}
          </span>
        </div>
        <input
          type="file"
          accept="image/*"
          className="hidden"
          onChange={(e) => setFile(e.target.files[0])}
        />
      </label>

      <button
        onClick={handleUpload}
        disabled={loading}
        className="w-full py-2 bg-indigo-600 text-white font-semibold rounded-lg shadow-md hover:bg-indigo-700 transition disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        {loading ? "⏳ Processing..." : "🚀 Mask My ID"}
      </button>

      {loading && (
        <div className="mt-4 flex justify-center items-center">
          <div className="w-6 h-6 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin"></div>
          <p className="ml-2 text-gray-700">Processing...</p>
        </div>
      )}
    </div>
  );
}

export default UploadForm;
