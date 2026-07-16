import { useEffect, useState } from "react";

import UploadCard from "../components/UploadCard/UploadCard";
import DocumentList from "../components/DocumentList/DocumentList";
import ChatBox from "../components/ChatBox/ChatBox";

import { api } from "../services/api";

import type { IndexedDocument } from "../types/document";

import "./HomePage.css";

export default function HomePage() {
  const [documents, setDocuments] = useState<IndexedDocument[]>([]);

  async function loadDocuments() {
    try {
      const { data } = await api.get<IndexedDocument[]>("/documents");

      setDocuments(data);
    } catch (error) {
      console.error("Failed to load documents", error);
    }
  }

  async function deleteDocument(storedFilename: string) {
    const confirmed = window.confirm(
      "Are you sure you want to delete this document?",
    );

    if (!confirmed) {
      return;
    }

    try {
      await api.delete(`/documents/${encodeURIComponent(storedFilename)}`);

      await loadDocuments();
    } catch (error) {
      console.error("Failed to delete document", error);
    }
  }

  useEffect(() => {
    loadDocuments();
  }, []);

  return (
    <div className="page">
      <aside className="sidebar">
        <UploadCard onUploadComplete={loadDocuments} />

        <DocumentList documents={documents} onDelete={deleteDocument} />
      </aside>

      <main className="main-content">
        <ChatBox />
      </main>
    </div>
  );
}
