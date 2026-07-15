export interface Source {
    filename: string;
    chunk_index: number;
}

export interface ChatRequest {
    question: string;
}

export interface ChatResponse {
    answer: string;
    sources: Source[];
}