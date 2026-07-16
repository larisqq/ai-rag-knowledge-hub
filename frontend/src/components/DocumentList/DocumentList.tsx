import type { IndexedDocument } from "../../types/document";

import Card from "../Card/Card";
import DocumentItem from "../DocumentItem/DocumentItem";

export default function DocumentList({
  documents,
}: {
  documents: IndexedDocument[];
}) {
  return (
    <Card title="Indexed Documents">
      {documents.length === 0 ? (
        <p>No documents uploaded.</p>
      ) : (
        documents.map((document) => (
          <DocumentItem key={document.filename} document={document} />
        ))
      )}
    </Card>
  );
}
