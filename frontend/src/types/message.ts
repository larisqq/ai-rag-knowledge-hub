export interface Message {
  id: string;

  role: "user" | "assistant";

  content: string;

  sources?: {
    filename: string;
    chunk_index: number;
  }[];
}