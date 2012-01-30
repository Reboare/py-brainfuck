from brainfuck import Brainfuck

try:
    from nltk.corpus import cmudict
    
    
except ImportError, e:
    print "Haiku parsing disabling!  To enable please install nltk"
    

def compliant_haiku(haiku_source):
        """Ensure that newlines remain and all 
        other punctuation has been stripped"""
        dict = cmudict.dict()
        haiku_lines = haiku_source.splitlines()
        syllables = []
        for line in haiku_lines:
            if line == "":
                continue
            sal=[]
            for word in line.split(" "):
                sal.append(len([x for x in dict[word][0] if x[-1].isdigit()]))
            syllables.append(sum(sal))
        pattern = [5,7,5]
        if len(syllables) % 3 == 0:
            while len(syllables) > 0:
                if syllables[:3] == pattern:
                    for x in range(2,-1,-1):
                        syllables.pop(x)
                else:
                    return False
        else:
            return False
        return True
    
compliant_haiku("beautiful jasmine\nyour lovely fragrance heals me\n\nevery morning\nremembering you\ndreaming of your lovely smile\nwhen will you come here")

class CherryBlossom(Brainfuck):
    """CherryBlossom Interpreter.  A language fundamentally identical to
    Brainfuck but with a haiku structure.  http://vivin.net/projects/cherryblossom/
    Issues:  -Strict parsing doesn't work!  some invalid programs will therefore parse
    """
    def __init__(self, source, strict_parsing = False):
        """At this point strict parsing does not work!  AVOID AVOID AVOID"""
        self.strict_parsing = strict_parsing
        Brainfuck.__init__(self, self.__convert(source))
    
    def __compliant_haiku(self, haiku_source):
        """Ensure that newlines remain and all 
        other punctuation has been stripped"""
        """Ensure that newlines remain and all 
        other punctuation has been stripped"""
        dict = cmudict.dict()
        haiku_lines = haiku_source.splitlines()
        syllables = []
        for line in haiku_lines:
            if line == "":
                continue
            sal=[]
            for word in line.split(" "):
                sal.append(len([x for x in dict[word][0] if x[-1].isdigit()]))
            syllables.append(sum(sal))
        pattern = [5,7,5]
        if len(syllables) % 3 == 0:
            while len(syllables) > 0:
                if syllables[:3] == pattern:
                    for x in range(2,-1,-1):
                        syllables.pop(x)
                else:
                    return False
        else:
            return False
        return True
        
        
    def __convert(self, source_data, strict = False):
        """Takes a Haiku source file and translates it into
        a set of brainfuck instructions"""
        
        #Cleans out the line of newlines
        #Might be a good idea here to actually see if it is a valid haiku
        #clean up this code dude
        cleaned = ""
        commands = []
        ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
        source = " ".join(source_data.splitlines())
        cleaned_line = "".join([x for x in source if x in ascii_letters])
        
        commands.extend(cleaned_line.split(" "))
        for cmd in commands:
            done = False
            for key, words in self.maps.iteritems():
                for word in words:
                    if word == cmd:
                        cleaned += key
                        done = True
                        break
                if done == True:
                    break
            if strict == True: 
                if done == False:
                    error = "Nonvalid Command used: %s" % (cmd)
                    raise SyntaxError(error)
                elif not self.__compliant_haiku(source_data):
                    raise SyntaxError("Not a valid Haiku")
        return cleaned
    
    
    
    maps = {
               ">" : ['above', 'ahead', 'atmosphere', 
                      'bird', 'birds', 'flew', 
                      'flies', 'flight', 'float', 
                      'floated', 'floating', 'floats',
                      'fly', 'flew', 'flying', 
                      'forward', 'front', 'heaven', 
                      'heavenly', 'height', 'high',
                      'higher', 'hill', 'hillside', 
                      'hilltop', 'mountain', 'mountainside', 
                      'mountaintop', 'push', 'pushed', 
                      'pushes', 'pushing', 'rise', 
                      'rises', 'rising', 'sky', 
                      'top', 'up', 'upward', 
                      'upwards'],
               "<" : ['back', 'backward', 'backwards', 
                      'behind', 'below', 'dip', 
                      'down', 'downwards', 'earth', 
                      'fall', 'falling', 'falls', 
                      'fell', 'ground', 'grounded', 
                      'land', 'landed', 'landing', 
                      'lands', 'low', 'lower', 
                      'lowered', 'lowering', 'lowers', 
                      'pull', 'rain', 'rained', 
                      'rainfall', 'raining', 'rains', 
                      'reverse', 'sink', 'sinking', 
                      'sinks', 'snake', 'snow', 
                      'snowed', 'snowfall', 'snowing', 
                      'snows', 'valley', 'waterfall'],
               "+" : ['alive', 'add', 'added', 'adding', 
                      'adds', 'beautified', 
                      'beautifies', 'beautiful', 'beautify', 
                      'beautifying', 
                      'beauty', 'butterfly', 'butterflies', 
                      'big', 'bigger', 'bloom', 'bloomed', 
                      'blooming', 'blooms', 'blossom', 
                      'blossoming', 'blossoms', 'caress', 
                      'caressed', 'caresses', 
                      'caressing', 'cherry-blossom', 'cherry-blossoms', 
                      'dawn', 'day', 'daybreak', 'days', 'dove', 
                      'doves', 'dream', 'dreaming', 
                      'dreams', 'dreamy', 'fat', 'fattening', 
                      'fatty', 'field', 'fields', 
                      'fire', 'flower', 'flowered', 'flowering', 
                      'flowers', 'fragrance', 
                      'fragrant', 'gain', 'gained', 'gains', 'get', 
                      'gets', 'getting', 
                      'good', 'grew', 'grow', 'growing', 'grows', 
                      'had', 'happiness', 'happy', 
                      'have', 'having', 'heal', 'healed', 'healing', 
                      'heals', 'heat', 'heated', 
                      'heats', 'hot', 'jasmine', 'learn', 'learning', 
                      'learns', 'life', 'live', 
                      'love', 'loved', 'lovely', 'loves', 'loving',
                       'lush', 'many', 'money', 
                      'more', 'morning', 'new', 'own', 'owned', 
                      'owning', 'owns', 'pleased', 
                      'pleasing', 'pleasure', 'positive', 'pretty', 
                      'rainbow', 'rainbows', 
                      'remember', 'remembered', 'remembering', 
                      'remembers', 'rose', 'roses', 
                      'rosy', 'smile', 'smiled', 'smiles', 'smiling', 
                      'spring', 'steam', 
                      'steamed', 'steams', 'steamy', 'summer', 'sun', 
                      'sunlight', 'sunlit', 
                      'sunray', 'sunrays', 'sunshine', 'sweet', 
                      'sweeten', 'sweetened', 'sweeter', 
                      'sweetly', 'sweets', 'warm', 'warmth', 
                      'wealth'],
                "-" : ['alone', 'autumn', 'anger', 'angry', 
                       'bad', 'barren', 'break', 'broke', 
                       'broken', 'cold', 'cool', 'chill', 
                       'chilled', 'chills', 'chilly', 'cried', 
                       'cry', 'crying', 'dark', 'darkening', 
                       'darker', 'dead', 'death', 'desolate', 
                       'desolation', 'depressed', 'depressing', 
                       'desert', 'deserts', 'die', 'dies', 
                       'dusk', 'dying', 'evening', 'evil', 'fear', 
                       'fearful', 'few', 'fog', 'fogged', 
                       'foggy', 'forget', 'forgetful', 'forgetting', 
                       'forgot', 'forgotten', 'forsake', 
                       'forsaken', 'freeze', 'freezing', 'freezes', 
                       'froze', 'frozen', 'fright', 
                       'frighten', 'frightened', 'frightening', 
                       'gloom', 'gloomy', 'greed', 'greedy', 
                       'ice', 'icy', 'less', 'lessen', 'lessened', 
                       'lone', 'lonely', 'lonesome', 'lose', 
                       'losing', 'loss', 'lost', 'melancholy', 
                       'miss', 'missed', 'misses', 'missing', 
                       'mist', 'mistake', 'mistaken', 'misted', 
                       'mists', 'misty', 'moon', 'moonlight', 
                       'moonlit', 'moonshine', 'nothing', 'night', 
                       'nightfall', 'nightmare', 'old', 'pain', 
                       'painful', 'poor', 'poverty', 'rage', 'remove', 
                       'removes', 'removing', 'sad', 'sadness', 
                       'scream', 'screamed', 'screams', 'screaming', 
                       'shrank', 'shrink', 'shrinking', 'shrinks', 
                       'shrunk', 'small', 'smaller', 'sorrow', 
                       'sorrowful', 'tear', 'tearful', 'teary', 'thin', 
                       'thins', 'thinned', 'thinning', 'ugliness', 
                       'ugly', 'winter', 'wither', 'withering', 'withers', 
                       'wound', 'wounded', 'wounds'],
                "[" : ['if', 'why', 'when', 'where', 'how', 
                       'who', 'what', 'inspect', 
                       'puzzle', 'question', 'mull', 
                       'riddle', 'decide', 'branch', 
                       'branched', 'branches', 'branching', 
                       'mulled', 'mulling', 'mulls', 
                       'decides', 'deciding', 'decided', 
                       'contemplate', 'contemplating', 
                       'contemplation', 'contemplated', 
                       'contemplates', 'think', 'thinking', 
                       'thought', 'thinks', 'choose', 'chose',
                        'choosing', 'chooses', 'wonder', 
                       'wondered', 'wondering', 'wonders'],
                "]" : ['return', 'home', 'reunite', 'returns', 
                       'returned', 'returning', 
                       'reunited', 'reunites', 'reuinting', 
                       'acknowledge', 'acknowledges', 
                       'acknowledged', 'acknowledging', 
                       'acknowledgement', 'homecoming', 
                       'retreat', 'retreating', 'retreats', 
                       'retreated', 'restore', 'restoring', 
                       'restored', 'restores', 'revisit', 
                       'revisited', 'revisiting', 'revisits', 
                       'rebound', 'rebounded', 'rebounding', 
                       'rebounds', 'boomerang'],
                "." : ['answer', 'answered', 'answering', 
                       'answers', 'art', 'artist', 
                       'author', 'birdsong', 'book', 
                       'brook', 'creek', 'display', 
                       'displaying', 'displays', 'flow', 
                       'flowing', 'flows', 'gave', 
                       'give', 'giving', 'laugh', 
                       'laughed', 'laughing', 'laughs', 
                       'laughter', 'letter', 'melodious', 
                       'melody', 'music', 'paint', 
                       'painter', 'painting', 'paints', 
                       'picture', 'poem', 'poet', 
                       'present', 'respond', 'result', 
                       'river', 'riverside', 'said', 
                       'say', 'saying', 'says', 
                       'show', 'showed', 'showing', 
                       'shows', 'sang', 'sight', 
                       'sing', 'singer', 'singing', 
                       'sings', 'speak', 'speaker', 
                       'speaking', 'speaks', 'spoke', 
                       'stream', 'view', 'views', 
                       'window', 'word', 'words', 
                       'write', 'writer', 'writes', 
                       'writing', 'wrote'],
                "," : ['absorb', 'absorbed', 'absorbing', 
                       'absorbs', 'accepted', 'accepting', 
                       'accepts', 'annex', 'annexed', 
                       'annexes', 'annexing', 'ask', 
                       'asked', 'asking', 'asks', 
                       'attract', 'attracted', 'attracting', 
                       'attracts', 'conquer', 'conquered', 
                       'conquering', 'conquers', 'ditch', 
                       'fill', 'filled','filling', 
                       'fills', 'hear', 'hearing', 
                       'hears', 'hole', 'in', 
                       'indoor', 'indoors', 'inside', 
                       'knew', 'know', 'knowing', 
                       'knowledge', 'knows', 'learn', 
                       'learned', 'learning', 'learns', 
                       'lesson', 'lessons', 'question',
                       'questioned', 'questioning', 
                       'questions', 'read', 'reader', 
                       'reading', 'reads', 'receive', 
                       'received', 'receives', 'receiving', 
                       'suck', 'sucked', 'sucking', 
                       'sucks', 'taken', 'takes', 
                       'taking', 'taught', 'teach', 
                        'teacher', 'teaching', 'took', 
                        'vortex', 'whirlpool'],
                "" : ['about', 'all', 'and', 'am', 'an', 'at', 'a', 'any', 'are', 'because', 
                      'be', 'by', 'came', 'can', 'come', 'could', 'did', 'do', 'does', 'every', 
                      'everything', 'for', 'from', 'go', 'he', 'her', 'hers', 'here', 'him', 'his', 
                      'in', 'i', 'is', 'it', 'man', 'me', 'mine', 'my', 'no', 'now', 'of', 'one', 
                      'on', 'or', 'our', 'ours', 'she', 'should', 'some', 'such', 'that', 'them', 
                      'then', 'the', 'their', 'theirs', 'there', 'they', 'this', 'to', 'to', 'us', 
                      'was', 'went', 'were', 'will', 'with', 'woman', 'would', 'yes', 'you', 'your',
                       'yours']
               }
