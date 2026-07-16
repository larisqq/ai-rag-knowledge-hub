import type { IndexedDocument } from "../../types/document";

import "./DocumentItem.css";

interface Props {
  document: IndexedDocument;
}

export default function DocumentItem({ document }: Props) {
  return (
    <div className="document-item">
      <div className="document-name">📄 {document.filename}</div>

      <div className="document-chunks">{document.chunks} chunks</div>
    </div>
  );
}
