import type { IndexedDocument } from "../../types/document";

import "./DocumentItem.css";

interface Props {
  document: IndexedDocument;

  onDelete: (storedFilename: string) => void;
}

export default function DocumentItem({ document, onDelete }: Props) {
  return (
    <div className="document-item">
      <div className="document-info">
        <div className="document-name">📄 {document.filename}</div>

        <div className="document-chunks">{document.chunks} chunks</div>
      </div>

      <button
        className="delete-button"
        onClick={() => onDelete(document.stored_filename)}
      >
        Delete
      </button>
    </div>
  );
}
