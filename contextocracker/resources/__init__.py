"""Utilities used to retrieve the paths to various coropora."""

from os.path import dirname, join


def brown_words_filtered() -> str:
    """Return the full path to a list of Brown words that are recognized by contexto."""
    parent_dir = dirname(__file__)
    file_name = "brown_words_filtered.txt"
    return join(parent_dir, file_name)


def words_alpha_unfiltered() -> str:
    """Return the full path to a list of 350k English words.

    Taken from https://github.com/dwyl/english-words
    """
    parent_dir = dirname(__file__)
    file_name = "words_alpha.txt"
    return join(parent_dir, file_name)


def words_alpha_filtered() -> str:
    """Return the full path to a list of words in 'words_alpha.txt' that contexto recognizes."""
    return join(dirname(__file__), "words_alpha_filtered.txt")


def brown_and_alpha_filtered() -> str:
    """Return the union of brown_words_filtered.txt and words_alpha_filtered.txt."""
    return join(dirname(__file__), "brown_and_word_list.txt")

def winning_words() -> list[str]:
    """Return the first 427 winning words (up until game #426)."""
    return ['banana', 'neighborhood', 'paper', 'farm', 'meat', 'computer', 'teacher', 'bike', 'mouse', 'bird', 'fun', 'university', 'car', 'bee', 'clock', 'work', 'history', 'glass', 'tv', 'road', 'head', 'apartment', 'beautiful', 'city', 'pen', 'dog', 'plate', 'diamond', 'wedding', 'soda', 'hair', 'queen', 'baseball', 'relationship', 'library', 'night', 'cell', 'piano', 'revenue', 'sister', 'potato', 'newspaper', 'street', 'bag', 'metal', 'family', 'garden', 'business', 'kitchen', 'mirror', 'health', 'country', 'video', 'christmas', 'space', 'hotel', 'luck', 'school', 'movie', 'company', 'trophy', 'text', 'money', 'idea', 'north', 'justice', 'image', 'sea', 'bedroom', 'answer', 'imagination', 'chair', 'baby', 'comma', 'prayer', 'lamp', 'boat', 'dream', 'choir', 'brain', 'orange', 'bakery', 'mail', 'chicken', 'headphone', 'coach', 'triangle', 'floor', 'king', 'day', 'app', 'student', 'window', 'shirt', 'rain', 'exam', 'judge', 'drink', 'market', 'talent', 'classroom', 'military', 'violin', 'tea', 'park', 'portrait', 'oil', 'menu', 'childhood', 'singer', 'time', 'stomach', 'friend', 'lion', 'hand', 'cabbage', 'water', 'mountain', 'book', 'eagle', 'income', 'cable', 'snow', 'cheese', 'throat', 'building', 'trip', 'engine', 'scarf', 'milkshake', 'apple', 'doctor', 'wave', 'error', 'fairy', 'needle', 'frog', 'toothpaste', 'fireman', 'zebra', 'employee', 'heart', 'watch', 'nature', 'challenge', 'economy', 'box', 'hospital', 'red', 'award', 'knife', 'garlic', 'drama', 'muscle', 'moon', 'tire', 'grasshopper', 'cereal', 'truck', 'shadow', 'calculator', 'horse', 'planet', 'strawberry', 'grass', 'telescope', 'purse', 'lobster', 'temperature', 'flag', 'butterfly', 'bus', 'puzzle', 'starfish', 'mushroom', 'eraser', 'band', 'factory', 'pasta', 'symphony', 'treasure', 'coffee', 'mermaid', 'spider', 'comedy', 'gym', 'guitar', 'magnet', 'egg', 'pumpkin', 'letter', 'story', 'documentary', 'ring', 'stock', 'bridge', 'pirate', 'tunnel', 'astronaut', 'opera', 'workout', 'restaurant', 'octopus', 'shark', 'airport', 'trailer', 'spoon', 'sun', 'metro', 'interview', 'pyramid', 'stamp', 'ship', 'speaker', 'jelly', 'salad', 'football', 'cow', 'postcard', 'innovation', 'word', 'feeling', 'sausage', 'language', 'bed', 'desk', 'asteroid', 'research', 'iceberg', 'design', 'star', 'sleep', 'massage', 'chart', 'fish', 'salon', 'energy', 'continent', 'game', 'cake', 'fries', 'molecule', 'valentine', 'gas', 'soap', 'flower', 'brush', 'galaxy', 'river', 'trash', 'ocean', 'animal', 'cafeteria', 'hallway', 'deer', 'plastic', 'grammar', 'soup', 'math', 'bathroom', 'toilet', 'stadium', 'art', 'elevator', 'system', 'goat', 'dishwasher', 'dentist', 'elephant', 'happiness', 'keyboard', 'forest', 'dolphin', 'rainbow', 'photo', 'train', 'backpack', 'cellphone', 'pillow', 'promotion', 'toothbrush', 'sock', 'science', 'microphone', 'candle', 'tree', 'paintbrush', 'necklace', 'programmer', 'basket', 'door', 'shoe', 'cloud', 'robot', 'parrot', 'light', 'kettle', 'perfume', 'sailor', 'volcano', 'cookie', 'circle', 'wig', 'church', 'tooth', 'yogurt', 'tourist', 'nose', 'mailbox', 'olive', 'drawer', 'pineapple', 'island', 'duck', 'castle', 'leaf', 'brick', 'honey', 'suitcase', 'flute', 'waffle', 'tie', 'wardrobe', 'society', 'string', 'friendship', 'pan', 'map', 'highway', 'music', 'silk', 'lemon', 'iron', 'giraffe', 'laptop', 'salmon', 'wallet', 'museum', 'freedom', 'joy', 'architect', 'hammer', 'blanket', 'rice', 'camera', 'pilot', 'room', 'bacteria', 'scarecrow', 'pet', 'gate', 'geography', 'sky', 'square', 'stone', 'table', 'clothes', 'community', 'evening', 'protein', 'cello', 'profit', 'sibling', 'spinach', 'article', 'village', 'diaper', 'steel', 'lawn', 'industry', 'carpet', 'sweet', 'bow', 'wheel', 'curtain', 'grocery', 'travel', 'sofa', 'melody', 'cinnamon', 'fabric', 'appliance', 'orchestra', 'vanilla', 'jacket', 'tax', 'wire', 'storm', 'cheddar', 'mouth', 'house', 'dollar', 'puppy', 'dish', 'refrigerator', 'helicopter', 'academy', 'patient', 'success', 'prince', 'hockey', 'emotion', 'campus', 'hall', 'month', 'battery', 'musical', 'payment', 'corn', 'magazine', 'avenue', 'gift', 'copper', 'compassion', 'smartphone', 'kangaroo', 'festival', 'constitution', 'lantern', 'marathon', 'yacht', 'mind', 'chorus', 'kidney', 'grapefruit', 'address']