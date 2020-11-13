# from gensim.summarization.summarizer import summarize

class SummaryUtil:

    @staticmethod
    def Summry_News(contents):
        
        summary = None
        
        if contents != None:
            content_split = contents.split('.')

            if len(content_split) > 3:
                    summary = '.'.join(content_split[:3])
            else:
                summary = '.'.join(content_split)
            
            return summary

        else:
            return None

