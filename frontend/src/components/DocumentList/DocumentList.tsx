import type { IndexedDocument } from "../../types/document";

import Card from "../Card/Card";
import DocumentItem from "../DocumentItem/DocumentItem";

import "./DocumentList.css";

interface Props {
  documents: IndexedDocument[];

  onDelete: (storedFilename: string) => void;
}

export default function DocumentList({ documents, onDelete }: Props) {
  return (
    <Card title="Indexed Documents">
      {documents.length === 0 ? (
        <p>No documents uploaded.</p>
      ) : (
        <div className="document-list">
          {documents.map((document) => (
            <DocumentItem
              key={document.stored_filename}
              document={document}
              onDelete={onDelete}
            />
          ))}
        </div>
      )}
    </Card>
  );
}
