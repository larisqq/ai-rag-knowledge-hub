import { useState } from "react";

import { api } from "../../services/api";

import Card from "../Card/Card";

import "./UploadCard.css";

interface Props {
  onUploadComplete: () => void;
}

export default function UploadCard({ onUploadComplete }: Props) {
  const [file, setFile] = useState<File | null>(null);

  const [uploading, setUploading] = useState(false);

  async function handleUpload() {
    if (!file || uploading) {
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
    <Card title="Upload Document">
      <div className="upload-card">
        <input
          type="file"
          accept=".pdf"
          onChange={(event) => setFile(event.target.files?.[0] ?? null)}
        />

        {file && <p className="selected-file">📄 {file.name}</p>}

        <button onClick={handleUpload} disabled={!file || uploading}>
          {uploading ? "Processing..." : "Upload"}
        </button>
      </div>
    </Card>
  );
}
