import type { IndexedDocument } from "../types/document";

interface Props {
  documents: IndexedDocument[];
}

export default function DocumentList({ documents }: Props) {
  return (
    <div>
      <h2>Indexed Documents</h2>

      {documents.length === 0 ? (
        <p>No documents uploaded.</p>
      ) : (
        <ul>
          {documents.map((document) => (
            <li key={document.filename}>
              📄 {document.filename} ({document.chunks} chunks)
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
