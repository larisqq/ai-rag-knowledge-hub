import { useEffect, useState } from "react";

import UploadCard from "../components/UploadCard/UploadCard";
import DocumentList from "../components/DocumentList/DocumentList";
import ChatBox from "../components/ChatBox/ChatBox";

import { api } from "../services/api";

import type { IndexedDocument } from "../types/document";

export default function HomePage() {
  const [documents, setDocuments] = useState<IndexedDocument[]>([]);

  async function loadDocuments() {
    const response = await api.get<IndexedDocument[]>("/documents");

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
