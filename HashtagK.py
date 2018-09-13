import glob
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


class Hashtag(object):
    """
    Hashtag Class
    """

    @staticmethod
    def sentence_to_find(word, files):
        """
        Check the keyword in the documents where it was found and and prepare the final string to append into html

        :param str word:
        :param dict files:
        :return:
        """

        txt_files = []
        txt_sentences = []
        final_line = ""
        for file in files["documents"]:
            txt_files.append(file)
        for txt_file in txt_files:
            file = open(txt_file, "r")
            for line in file:
                if word in line or word.title() in line:
                    format_text = "<br/><p>".join(line.split("\n"))
                    split_to_highlight = format_text.split(" ")
                    for split_word in split_to_highlight:
                        clean_word = split_word.replace(".", "").replace(",", "").replace("!", "").replace("?", "").\
                            replace("'s", "")
                        if clean_word == word or clean_word == word.title():
                            final_line += "<b>" + " " + word + "</b>"
                        else:
                            final_line += " " + split_word
                    txt_sentences.append(final_line)
                    final_line = ""
            file.close()
        return txt_sentences

    def generate_html_document(self, values, max_records_to_show):
        """
        Generates the html in the current dir, this will trigger the sentence finder method
        :param dict values:
        :param int max_records_to_show:
        :return:
        """

        file = open('MatchReport.html', 'w')
        message = """
        <html>
        <head>
            <style>
                table, th, td {
                    border: thin solid black;
                    border-collapse: collapse;
                    font-weight: 400;
                }
                th, td {
                    padding: 5px;
                    text-align: left;    
                }
            </style>
        </head>
        <body>
            <table style = "width:100%; font-weight:normal;">
                <tr>
                <th>Word#</th>
                <th>Documents</th>
                <th>Sentences containing the word</th>
                </tr>
        """
        i = 0
        for k, v in values.items():
            i += 1
            sentences = self.sentence_to_find(k, v)
            message += """
            <tr>
            <th>{word}</th>
            <th>{documents}</th>
            <th>{sentence}</th>
            </tr>
            """.format(**{
                "word": k,
                "documents": '\n'.join(v["documents"]),
                "sentence": '\n'.join(sentences),
            })
            if i == max_records_to_show:
                break

        message += "</table></body></html>"
        file.write(message)
        file.close()

    def grab_text_from_documents(self):
        """
        Get all files in TXT file and store them into a list
        Uses NLTK (natural language toolkit) to avoid common words useless for search

        :return:
        """
        words = {}
        txt_files = []
        word_to_exclude = ["i", ""]
        max_records_to_show = 10

        for file in glob.glob("docs/*.txt"):
            txt_files.append(file)
        for txt_file in txt_files:
            file = open(txt_file, "r")
            for line in file:
                tokens = nltk.word_tokenize(line.lower())
                tagged = nltk.pos_tag(tokens)
                for word, word_type in tagged:
                    if word_type == "NN" and word_type not in word_to_exclude:
                        w = word
                        if w in words:
                            words[w]["counter"] += 1
                        else:
                            words[w] = {
                                "counter": 1
                            }
                        if "documents" not in words[w]:
                            words[w]["documents"] = [txt_file]
                        else:
                            if txt_file not in words[w]["documents"]:
                                words[w]["documents"].append(txt_file)
            file.close()
        sorted_dict_results = {}
        for a in sorted(words.keys(), key=lambda y: words[y]['counter'], reverse=True):
            sorted_dict_results[a] = words[a]

        self.generate_html_document(sorted_dict_results, max_records_to_show)
        print(sorted_dict_results)


if __name__ == "__main__":
    app = Hashtag()
    app.grab_text_from_documents()
