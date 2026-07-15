import { useState } from "react";
import { api } from "../services/api";

interface Props {
  onUploadComplete: () => void;
}

export default function UploadCard({ onUploadComplete }: Props) {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);

  async function handleUpload() {
    if (!file) {
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {
      setUploading(true);

      await api.post("/documents/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setFile(null);

      onUploadComplete();
    } catch (error) {
      console.error("Upload failed", error);
    } finally {
      setUploading(false);
    }
  }

  return (
    <div>
      <h2>Upload Document</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(event) => setFile(event.target.files?.[0] ?? null)}
      />

      <button onClick={handleUpload} disabled={!file || uploading}>
        {uploading ? "Processing..." : "Upload"}
      </button>
    </div>
  );
}
