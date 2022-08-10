"""
    Classification file for AIDI 2004 Project
"""

import preprocess


def predict_review(model, new_sentences, tokenizer):
        result_dict = dict()
        result_dict['Input'] = new_sentences
        
        new_sentences = preprocess.preprocess(new_sentences) # preprocess input sentence

        prediction_token = tokenizer.transform([new_sentences]) 
    
        classes = model.predict(prediction_token)  # predict on sentence
    
        # Print its predicted class\n",
        if classes[0] == 1:
            result_dict['Result'] = "Unreliable, Fake News"
            _res  = "Unreliable, Fake News"
            #print("Fake News")
        else:
            result_dict['Result'] = "Reliable News"
            _res = "Reliable News"
            #print("Not Fake News")
        result_dict['Probability'] = classes[0]
        
        #return result_dict['Input'], result_dict['Input'], result_dict['Probability']\n",
        return _res