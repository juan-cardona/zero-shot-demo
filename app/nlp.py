from transformers import (
    pipeline
)


class NLP:

    def zero_shot(self, df):
        print('well at least i got here...')
        classifier = pipeline("zero-shot-classification")
        candidate_labels = ["food safety", "politics",
                            "reputation", "quality", "corruption", "sales"]
        candidate_results = [0, 0, 0, 0, 0, 0]
        data = {}
        value_id = 0

        for sent in df['tweet'].values:
            # To do multi-class classification, simply pass multi_class=True.
            # In this case, the scores will be independent, but each will fall between 0 and 1.
            res = classifier(sent, candidate_labels, multi_class=True)

            data[value_id] = {}
            data[value_id]['Tweet'] = sent
            data[value_id]['Label'] = res['labels']
            data[value_id]['Score'] = res['scores']
            value_id += 1

            print_flag = 0
            for index, score in enumerate(res['scores']):
                if score > 0.5:
                    if res['labels'][index] == 'food safety':
                        candidate_results[0] = candidate_results[0] + 1
                    if res['labels'][index] == 'politics':
                        candidate_results[1] = candidate_results[1] + 1
                    if res['labels'][index] == 'reputation':
                        candidate_results[2] = candidate_results[2] + 1
                    if res['labels'][index] == 'quality':
                        candidate_results[3] = candidate_results[3] + 1
                    if res['labels'][index] == 'corruption':
                        candidate_results[4] = candidate_results[4] + 1
                    if res['labels'][index] == 'sales':
                        candidate_results[5] = candidate_results[5] + 1

                    if print_flag == 0:
                        print(sent)
                        print(res['labels'])
                        print(res['scores'])
                        print()
                        print_flag = 1
        return data
