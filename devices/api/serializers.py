from rest_framework import serializers

from users.models import user

from devices.models import (
    devices
)


class Create_device_record_serializer(serializers.ModelSerializer):

    class Meta:
        model = devices
        fields = '__all__'
        extra_kwargs ={
            'owner':{'required':False},
            'parameter1': {'required': False},
            'parameter2': {'required': False},
            'parameter3': {'required': False},
            'parameter4': {'required': False},
            'parameter5': {'required': False},
            'parameter6': {'required': False},
            'parameter7': {'required': False},
            'parameter8': {'required': False},
            'parameter9': {'required': False},
            'parameter10': {'required': False},
            'parameter11': {'required': False},
            'parameter12': {'required': False},
            'parameter13': {'required': False},
            'parameter14': {'required': False},
            'parameter15': {'required': False},
            'parameter16': {'required': False},
            'parameter17': {'required': False},
            'parameter18': {'required': False},
            'parameter19': {'required': False},
            'parameter20': {'required': False},
            'parameter21': {'required': False},
            'parameter22': {'required': False},
            'parameter23': {'required': False},
            'parameter24': {'required': False},
            'parameter25': {'required': False},
            'parameter26': {'required': False},
            'parameter27': {'required': False},
            'parameter28': {'required': False},
            'parameter29': {'required': False},
            'parameter30': {'required': False},
            'parameter31': {'required': False},
            'parameter32': {'required': False},
            'parameter33': {'required': False},
            'parameter34': {'required': False},
            'parameter35': {'required': False},
            'parameter36': {'required': False},
            'parameter37': {'required': False},
            'parameter38': {'required': False},
            'parameter39': {'required': False},
            'parameter40': {'required': False},
            'parameter41': {'required': False},
            'parameter42': {'required': False},
            'parameter43': {'required': False},
            'parameter44': {'required': False},
            'parameter45': {'required': False},
            'parameter46': {'required': False},
            'parameter47': {'required': False},
            'parameter48': {'required': False},
            'parameter49': {'required': False},
            'parameter50': {'required': False},
            'parameter51': {'required': False},
            'parameter52': {'required': False},
            'parameter53': {'required': False},
            'parameter54': {'required': False},
            'parameter55': {'required': False},
            'parameter56': {'required': False},
            'parameter57': {'required': False},
            'parameter58': {'required': False},
            'parameter59': {'required': False},
            'parameter60': {'required': False},
            'parameter61': {'required': False},
            'parameter62': {'required': False},
            'parameter63': {'required': False},
            'parameter64': {'required': False},
            'parameter65': {'required': False},
            'parameter66': {'required': False},
            'parameter67': {'required': False},
            'parameter68': {'required': False},
            'parameter69': {'required': False},
            'parameter70': {'required': False},
            'parameter71': {'required': False},
            'parameter72': {'required': False},
            'parameter73': {'required': False},
            'parameter74': {'required': False},
            'parameter75': {'required': False},
            'parameter76': {'required': False},
            'parameter77': {'required': False},
            'parameter78': {'required': False},
            'parameter79': {'required': False},
            'parameter80': {'required': False},
            'parameter81': {'required': False},
            'parameter82': {'required': False},
            'parameter83': {'required': False},
            'parameter84': {'required': False},
            'parameter85': {'required': False},
            'parameter86': {'required': False},
            'parameter87': {'required': False},
            'parameter88': {'required': False},
            'parameter89': {'required': False},
            'parameter90': {'required': False},
            'parameter91': {'required': False},
            'parameter92': {'required': False},
            'parameter93': {'required': False},
            'parameter94': {'required': False},
            'parameter95': {'required': False},
            'parameter96': {'required': False},
            'parameter97': {'required': False},
            'parameter98': {'required': False},
            'parameter99': {'required': False},
            'parameter100': {'required': False},
            'parameter101': {'required': False},
            'parameter102': {'required': False},
            'parameter103': {'required': False},
            'parameter104': {'required': False},
            'parameter105': {'required': False},
            'parameter106': {'required': False},
            'parameter107': {'required': False},
            'parameter108': {'required': False},
            'parameter109': {'required': False},
            'parameter110': {'required': False},
            'parameter111': {'required': False},
            'parameter112': {'required': False},
            'parameter113': {'required': False},
            'parameter114': {'required': False},
            'parameter115': {'required': False},
            'parameter116': {'required': False},
            'parameter117': {'required': False},
            'parameter118': {'required': False},
            'parameter119': {'required': False},
            'parameter120': {'required': False},
            'parameter121': {'required': False},
            'parameter122': {'required': False},
            'parameter123': {'required': False},
            'parameter124': {'required': False},
            'parameter125': {'required': False},
            'parameter126': {'required': False},
            'parameter127': {'required': False},
            'parameter128': {'required': False},
            'parameter129': {'required': False},
            'parameter130': {'required': False},
            'parameter131': {'required': False},
            'parameter132': {'required': False},
            'parameter133': {'required': False},
            'parameter134': {'required': False},
            'parameter135': {'required': False},
            'parameter136': {'required': False},
            'parameter137': {'required': False},
            'parameter138': {'required': False},
            'parameter139': {'required': False},
            'parameter140': {'required': False},
            'parameter141': {'required': False},
            'parameter142': {'required': False},
            'parameter143': {'required': False},
            'parameter144': {'required': False},
            'parameter145': {'required': False},
            'parameter146': {'required': False},
            'parameter147': {'required': False},
            'parameter148': {'required': False},
            'parameter149': {'required': False},
            'parameter150': {'required': False},
            'parameter151': {'required': False},
            'parameter152': {'required': False},
            'parameter153': {'required': False},
            'parameter154': {'required': False},
            'parameter155': {'required': False},
            'parameter156': {'required': False},
            'parameter157': {'required': False},
            'parameter158': {'required': False},
            'parameter159': {'required': False},
            'parameter160': {'required': False},
            'parameter161': {'required': False},
            'parameter162': {'required': False},
            'parameter163': {'required': False},
            'parameter164': {'required': False},
            'parameter165': {'required': False},
            'parameter166': {'required': False},
            'parameter167': {'required': False},
            'parameter168': {'required': False},
            'parameter169': {'required': False},
            'parameter170': {'required': False},
            'parameter171': {'required': False},
            'parameter172': {'required': False},
            'parameter173': {'required': False},
            'parameter174': {'required': False},
            'parameter175': {'required': False},
            'parameter176': {'required': False},
            'parameter177': {'required': False},
            'parameter178': {'required': False},
            'parameter179': {'required': False},
            'parameter180': {'required': False},
            'parameter181': {'required': False},
            'parameter182': {'required': False},
            'parameter183': {'required': False},
            'parameter184': {'required': False},
            'parameter185': {'required': False},
            'parameter186': {'required': False},
            'parameter187': {'required': False},
            'parameter188': {'required': False},
            'parameter189': {'required': False},
            'parameter190': {'required': False},
            'parameter191': {'required': False},
            'parameter192': {'required': False},
            'parameter193': {'required': False},
            'parameter194': {'required': False},
            'parameter195': {'required': False},
            'parameter196': {'required': False},
            'parameter197': {'required': False},
            'parameter198': {'required': False},
            'parameter199': {'required': False},
            'parameter200': {'required': False},
            'parameter201': {'required': False},
            'parameter202': {'required': False},
            'parameter203': {'required': False},
            'parameter204': {'required': False},
            'parameter205': {'required': False},
            'parameter206': {'required': False},
            'parameter207': {'required': False},
            'parameter208': {'required': False},
            'parameter209': {'required': False},
            'parameter210': {'required': False},
            'parameter211': {'required': False},
            'parameter212': {'required': False},
            'parameter213': {'required': False},
            'parameter214': {'required': False},
            'parameter215': {'required': False},
            'parameter216': {'required': False},
            'parameter217': {'required': False},
            'parameter218': {'required': False},
            'parameter219': {'required': False},
            'parameter220': {'required': False},
            'parameter221': {'required': False},
            'parameter222': {'required': False},
            'parameter223': {'required': False},
            'parameter224': {'required': False},
            'parameter225': {'required': False},
            'parameter226': {'required': False},
            'parameter227': {'required': False},
            'parameter228': {'required': False},
            'parameter229': {'required': False},
            'parameter230': {'required': False},
            'parameter231': {'required': False},
            'parameter232': {'required': False},
            'parameter233': {'required': False},
            'parameter234': {'required': False},
            'parameter235': {'required': False},
            'parameter236': {'required': False},
            'parameter237': {'required': False},
            'parameter238': {'required': False},
            'parameter239': {'required': False},
            'parameter240': {'required': False},
            'parameter241': {'required': False},
            'parameter242': {'required': False},
            'parameter243': {'required': False},
            'parameter244': {'required': False},
            'parameter245': {'required': False},
            'parameter246': {'required': False},
            'parameter247': {'required': False},
            'parameter248': {'required': False},
            'parameter249': {'required': False},
            'parameter250': {'required': False},
            'parameter251': {'required': False},
            'parameter252': {'required': False},
            'parameter253': {'required': False},
            'parameter254': {'required': False},
            'parameter255': {'required': False},
            'parameter256': {'required': False},
            'parameter257': {'required': False},
            'parameter258': {'required': False},
            'parameter259': {'required': False},
            'parameter260': {'required': False},
            'parameter261': {'required': False},
            'parameter262': {'required': False},
            'parameter263': {'required': False},
            'parameter264': {'required': False},
            'parameter265': {'required': False},
            'parameter266': {'required': False},
            'parameter267': {'required': False},
            'parameter268': {'required': False},
            'parameter269': {'required': False},
            'parameter270': {'required': False},
            'parameter271': {'required': False},
            'parameter272': {'required': False},
            'parameter273': {'required': False},
            'parameter274': {'required': False},
            'parameter275': {'required': False},
            'parameter276': {'required': False},
            'parameter277': {'required': False},
            'parameter278': {'required': False},
            'parameter279': {'required': False},
            'parameter280': {'required': False},
            'parameter281': {'required': False},
            'parameter282': {'required': False},
            'parameter283': {'required': False},
            'parameter284': {'required': False},
            'parameter285': {'required': False},
            'parameter286': {'required': False},
            'parameter287': {'required': False},
            'parameter288': {'required': False},
            'parameter289': {'required': False},
            'parameter290': {'required': False},
            'parameter291': {'required': False},
            'parameter292': {'required': False},
            'parameter293': {'required': False},
            'parameter294': {'required': False},
            'parameter295': {'required': False},
            'parameter296': {'required': False},
            'parameter297': {'required': False},
            'parameter298': {'required': False},
            'parameter299': {'required': False},
            'parameter300': {'required': False},
            'parameter301': {'required': False},
            'parameter302': {'required': False},
            'parameter303': {'required': False},
            'parameter304': {'required': False},
            'parameter305': {'required': False},
            'parameter306': {'required': False},
            'parameter307': {'required': False},
            'parameter308': {'required': False},
            'parameter309': {'required': False},
            'parameter310': {'required': False},
            'parameter311': {'required': False},
            'parameter312': {'required': False},
            'parameter313': {'required': False},
            'parameter314': {'required': False},
            'parameter315': {'required': False}

        }

class ViewDevicesRecords_Serializer(serializers.ModelSerializer):

    class Meta:
        model = devices
        fields = '__all__'


class View_filteredDevices_serializer(serializers.ModelSerializer):

    class Meta:
        model = devices
        fields = '__all__'
            # 'owner',
            # 'ID_of_device',
            # 'Time_send',
            # 'x',
            # 'y',
            # 'z',
            # 'roll',
            # 'pitch',
            # 'yaw',
            # 'psi',
            # 'theta',
            # 'phi',
            # 'labeled'




