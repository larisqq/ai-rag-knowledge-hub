from langchain_text_splitters import RecursiveCharacterTextSplitter


class Chunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=1000,

            chunk_overlap=200,

            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]

        )

    def split(self, pages):

        chunks = []

        for page in pages:

            texts = self.splitter.split_text(page["text"])

            for text in texts:

                chunks.append({

                    "page": page["page"],

                    "content": text

                })

        return chunks


chunker = Chunker()