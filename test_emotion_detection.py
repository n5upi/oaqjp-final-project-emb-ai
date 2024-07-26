from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
 
    def test_emotion_detector(self):
        # Test case for joy emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['label'], 'SENT_JOY')
    
        # Test case for anger emotion
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['label'], 'SENT_ANGER')
    
        # Test case for disgust emotion
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['label'], 'SENT_DISGUST')

        # Test case for sadness emotion
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['label'], 'SENT_SADNESS')

        # Test case for fear emotion
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['label'], 'SENT_FEAR')

unittest.main()