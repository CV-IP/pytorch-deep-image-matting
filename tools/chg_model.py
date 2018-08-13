import torch
import collections

x = torch.load('../model/vgg16-397923af.pth')

val = collections.OrderedDict()
val['conv1_1.weight'] = torch.cat((x['features.0.weight'], torch.zeros(64, 1, 3, 3)), 1)

replace = {	u'features.0.bias'   : 'conv1_1.bias',
		u'features.2.weight' : 'conv1_2.weight',
		u'features.2.bias'   : 'conv1_2.bias',
		u'features.5.weight' : 'conv2_1.weight',
		u'features.5.bias'   : 'conv2_1.bias',
		u'features.7.weight' : 'conv2_2.weight',
		u'features.7.bias'   : 'conv2_2.bias',
		u'features.10.weight': 'conv3_1.weight',
		u'features.10.bias'  : 'conv3_1.bias',
		u'features.12.weight': 'conv3_2.weight',
		u'features.12.bias'  : 'conv3_2.bias',
		u'features.14.weight': 'conv3_3.weight',
		u'features.14.bias'  : 'conv3_3.bias',
		u'features.17.weight': 'conv4_1.weight',
		u'features.17.bias'  : 'conv4_1.bias',
		u'features.19.weight': 'conv4_2.weight',
		u'features.19.bias'  : 'conv4_2.bias',
		u'features.21.weight': 'conv4_3.weight',
		u'features.21.bias'  : 'conv4_3.bias',
		u'features.24.weight': 'conv5_1.weight',
		u'features.24.bias'  : 'conv5_1.bias',
		u'features.26.weight': 'conv5_2.weight',
		u'features.26.bias'  : 'conv5_2.bias',
		u'features.28.weight': 'conv5_3.weight',
		u'features.28.bias'  : 'conv5_3.bias'
	}

for key in replace.keys():
    print(key, replace[key])
    val[replace[key]] = x[key]

y = {}
y['state_dict'] = val
y['epoch'] = 0
torch.save(y, '../model/vgg_state_dict.pth')
