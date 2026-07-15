import { useEffect, useState } from "react";

import { api } from "../services/api";

import DocumentList from "../components/DocumentList";
import UploadCard from "../components/UploadCard";
import ChatBox from "../components/ChatBox";

import type { IndexedDocument } from "../types/document";

export default function HomePage() {
  const [documents, setDocuments] = useState<IndexedDocument[]>([]);

  async function loadDocuments() {
    const response = await api.get("/documents");

    setDocuments(response.data);
  }

  useEffect(() => {
    loadDocuments();
  }, []);

  return (
    <div>
      <h1>AI Knowledge Hub</h1>

      <UploadCard onUploadComplete={loadDocuments} />

      <DocumentList documents={documents} />
      <ChatBox />
    </div>
  );
}
