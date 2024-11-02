import sys
from pprint import pprint

import yaml

text = """
MICKEY: It's a spaceship. Brilliant! I got a spaceship on my first go.
ROSE: It looks kind of abandoned. Anyone on board?
DOCTOR: Nah, nothing here. Well, nothing dangerous. Well, not that dangerous. You know what, I'll just have a quick scan, in case there's anything dangerous.
ROSE: So, what's the date? How far we gone?
DOCTOR: About three thousand years into your future, give or take.
DOCTOR: 51st century. Diagmar Cluster, you're a long way from home, Mickey. Two and a half galaxies.
ROSE: Mickey Smith, meet the universe. See anything you like?
MICKEY: It's so realistic!
DOCTOR: Dear me, had some cowboys in here. Got a ton of repair work going on. Now that's odd. Look at that. All the warp engines are going. Full capacity. There's enough power running through this ship to punch a hole in the universe, but we're not moving. So where's all that power going?
ROSE: Where'd all the crew go?
DOCTOR: Good question. No life readings on board.
ROSE: Well, we're in deep space. They didn't just nip out for a quick fag.
DOCTOR: No, I've checked all the smoking pods. Can you smell that?
ROSE: Yeah, someone's cooking.
MICKEY: Sunday roast, definitely.
"""

text2 = """
(The Doctor's village clothes are scattered on the floor, and a nearly empty bowl of fish fingers and custard is on the console. There are footsteps on the stairs. Her bow-tied young Doctor smiles at her.)
CLARA: Doctor!
DOCTOR: Hello.
CLARA: You're young again. You're okay. You didn't even change your face.
DOCTOR: Ha! It's started. I can't stop it now. This is just the reset. A whole new regeneration cycle. Ooo.
(He finishes his custard.)
DOCTOR: Taking a bit longer. Just breaking it in. Oh. Oh. Gah.
(He starts the Tardis' engines.)
DOCTOR: It all just disappears, doesn't it? Everything you are, gone in a moment, like breath on a mirror. Any moment now, he's a-coming.
CLARA: Who's coming?
DOCTOR: The Doctor.
CLARA: But you, you are the Doctor.
DOCTOR: Yep, and I always will be.
(His hands are glowing.)
DOCTOR: But times change, and so must I.
(The Doctor sees a young Amy Pond run up the stairs, laughing.)
DOCTOR: Amelia?
CLARA: Who's Amelia?
DOCTOR: The first face this face saw. We all change, when you think about it. We're all different people all through our lives. And that's okay, that's good, you've got to keep moving, so long as you remember all the people that you used to be. I will not forget one line of this. Not one day. I swear. I will always remember when the Doctor was me.
(Then he sees a vision of a red-haired woman with black painted fingernails walk down the stairs to him.)
AMY: Raggedy man. Good night.
(They touch each others cheeks, and she disappears. The Doctor removes his bow tie and drops it on the floor. His face is in pain.)
CLARA: No, no.
DOCTOR: Hey.
CLARA: Please don't change.
(The Doctor jerks backwards as Matt Smith and then forwards as Peter Capaldi. Tall, grey haired, piercing blue eyes and a Scottish burr. My kind of man. The new Doctor and Clara stare into each others eyes, then he jerks back and forward again.)
DOCTOR: Kidneys! I've got new kidneys. I don't like the colour.
CLARA: Of your kidneys?
(The Tardis starts lurching from side to side.)
CLARA: What's happening?
DOCTOR: We're probably crashing. Oh!
CLARA: Into what?
DOCTOR: Stay calm. Just one question. Do you happen to know how to fly this thing? 
"""

text3 ="""
BAINES: We'll blast them into dust, then fuse the dust into glass, then shatter them all over again.
(The spaceship door opens to admit -)
DOCTOR: Just
(A boom rocks the ship, and he lurches against a column of switches.)
DOCTOR: Just stop the bombardment. That's all I'm asking. I'll do anything you want, just, just stop.
BAINES: Say please.
DOCTOR: Please.
(Jenny activates a control.)
JENNY: Wait a minute. (sniff) Still human.
DOCTOR: Now I can't, I can't pretend to understand, not for a second, but I want you to know I'm innocent in all this. He made me John Smith. It's not like I had any control over it.
(He runs his hands over more switches.)
JENNY: He didn't just make himself human. He made himself an idiot.
BAINES: Same thing, isn't it?
DOCTOR: I don't care about this Doctor and your family. I just want you to go. So I've made my choice. You can have him. Just take it, please! Take him away.
(The Doctor holds out the watch.)
BAINES: At last.
(Baines takes the watch with one hand, and the Doctor's lapels by the other.)
BAINES: Don't think that saved your life.
(He pushes the Doctor away. More switches get activated as the Doctor falls against the wall.)
BAINES: Family of Mine, now we shall have the lives of a Time Lord.
(Baines opens the watch and they all sniff deeply.)
BAINES: It's empty!
DOCTOR: Where's it gone?
BAINES: You tell me.
(Baines throws the watch to the Doctor, who catches it without looking.)
DOCTOR: Oh, I think the explanation might be you've been fooled by a simple olfactory misdirection. Little bit like ventriloquism of the nose. It's an elementary trick in certain parts of the galaxy. But it has got to be said, I don't like the looks of that hydroconometer. It seems to be indicating you've got energy feedback all the way through the retrostabilisers feeding back into the primary heat converters. Oh. Because if there's one thing you shouldn't have done, you shouldn't have let me press all those buttons. But, in fairness, I will give you one word of advice. Run.
(The Doctor runs out of the ship as alarms start to sound.)
BAINES: Get out! Get out! 
"""


class Message:
    user: str
    text: str
    def __repr__(self) -> str:
        return f"Message({self.user}, {self.text})"



message_lines = [x for x in text3.split("\n")]


def line_to_message(line: str):
    if not ":" in line:
        return Message()
    name = line.split(":")[0].strip()
    message = line.split(":")[1].strip()
    messageObj = Message()
    messageObj.user = name
    messageObj.text = message
    return vars(messageObj)


lines = filter(lambda x: ":" in x, message_lines)
messages = list(map(line_to_message, lines))
pprint(messages)
yaml.dump(messages, sys.stdout)



