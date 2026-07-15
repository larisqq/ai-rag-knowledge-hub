export interface ChatSource {
    filename: string;
    chunk_index: number;
}

export interface ChatResponse {
    answer: string;
    sources: ChatSource[];
}