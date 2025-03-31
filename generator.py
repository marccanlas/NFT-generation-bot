from itertools import count
from progressbar import progressbar
import json
import os
op_path = os.path.join('./json')
i = 0
count = 3
# progress = progressbar.ProgressBar()
for n in range(count):
	print("n", n)
	f = open(os.path.join(op_path, str(n)), "r")
	content = f.read()
	f.close()
	data = json.loads(content)
	image_url = "https://ipfs.io/ipfs/QmNjShfqAreSRetqXf1VowwqYA79KXU92Rq2mcvyqbtkfB/"+str(i)+".png"
	data['image'] = image_url
	f = open(os.path.join(op_path, str(n)), "w")
	f.write(json.dumps(data))
	# data['image'] = image_url
	# json_object = json.dumps(data)
	# with open(str(i+1), "w") as outfile:
	# 	json.dump(data, outfile)
	f.close()
	i += 1