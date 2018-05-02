# yupik-tts
The planned layout

1) Segment a body of text into words
2) Fuctions that segment words into unit-level
ex. pissuryullrunrituk -> pissur yull run ri tuk
  - elongated vowel ending phonemes and consonant ending morphemes occur in a full second
  - all other vowel endings and endings gemination occur in 1/4 second
3) Search for phoneme audio clip
4) Concatenate phoneme sounds to form a word


audiofiles directory
any unit file with a 1 shows a 'hard' consonant so rr instead of r

advice on pitch replication:
dynamic time warping
time scaling — frequency scale followed by resampling

change the resampling factor
find a pitch of utterance
do frequency scaling of 440 divided by that pitch

time scale of 1 over duration
resampling by one over the duration

estimation of f0 in the frame
time varying frequency scale to pull out pitch variation
time scaling as a second pass

kalman filter
