from django.shortcuts import render
from django.utils import timezone

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from rest_framework.generics import CreateAPIView, ListAPIView


from .api.serializers import (
    Create_device_record_serializer,
    ViewDevicesRecords_Serializer,
    View_filteredDevices_serializer
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import (
    devices
)
from users.models import user

class Device_Create_recordAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = Create_device_record_serializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            creator = user.objects.get(username=request.user.username)
            ID_of_device = serializer.data['ID_of_device']
            labeled = serializer.data['labeled']
            parameter1 = serializer.data['parameter1']
            parameter2 = serializer.data['parameter2']
            parameter3 = serializer.data['parameter3']
            parameter4 = serializer.data['parameter4']
            parameter5 = serializer.data['parameter5']
            parameter6 = serializer.data['parameter6']
            parameter7 = serializer.data['parameter7']
            parameter8 = serializer.data['parameter8']
            parameter9 = serializer.data['parameter9']
            parameter10 = serializer.data['parameter10']
            parameter11 = serializer.data['parameter11']
            parameter12 = serializer.data['parameter12']
            parameter13 = serializer.data['parameter13']
            parameter14 = serializer.data['parameter14']
            parameter15 = serializer.data['parameter15']
            parameter16 = serializer.data['parameter16']
            parameter17 = serializer.data['parameter17']
            parameter18 = serializer.data['parameter18']
            parameter19 = serializer.data['parameter19']
            parameter20 = serializer.data['parameter20']
            parameter21 = serializer.data['parameter21']
            parameter22 = serializer.data['parameter22']
            parameter23 = serializer.data['parameter23']
            parameter24 = serializer.data['parameter24']
            parameter25 = serializer.data['parameter25']
            parameter26 = serializer.data['parameter26']
            parameter27 = serializer.data['parameter27']
            parameter28 = serializer.data['parameter28']
            parameter29 = serializer.data['parameter29']
            parameter30 = serializer.data['parameter30']
            parameter31 = serializer.data['parameter31']
            parameter32 = serializer.data['parameter32']
            parameter33 = serializer.data['parameter33']
            parameter34 = serializer.data['parameter34']
            parameter35 = serializer.data['parameter35']
            parameter36 = serializer.data['parameter36']
            parameter37 = serializer.data['parameter37']
            parameter38 = serializer.data['parameter38']
            parameter39 = serializer.data['parameter39']
            parameter40 = serializer.data['parameter40']
            parameter41 = serializer.data['parameter41']
            parameter42 = serializer.data['parameter42']
            parameter43 = serializer.data['parameter43']
            parameter44 = serializer.data['parameter44']
            parameter45 = serializer.data['parameter45']
            parameter46 = serializer.data['parameter46']
            parameter47 = serializer.data['parameter47']
            parameter48 = serializer.data['parameter48']
            parameter49 = serializer.data['parameter49']
            parameter50 = serializer.data['parameter50']
            parameter51 = serializer.data['parameter51']
            parameter52 = serializer.data['parameter52']
            parameter53 = serializer.data['parameter53']
            parameter54 = serializer.data['parameter54']
            parameter55 = serializer.data['parameter55']
            parameter56 = serializer.data['parameter56']
            parameter57 = serializer.data['parameter57']
            parameter58 = serializer.data['parameter58']
            parameter59 = serializer.data['parameter59']
            parameter60 = serializer.data['parameter60']
            parameter61 = serializer.data['parameter61']
            parameter62 = serializer.data['parameter62']
            parameter63 = serializer.data['parameter63']
            parameter64 = serializer.data['parameter64']
            parameter65 = serializer.data['parameter65']
            parameter66 = serializer.data['parameter66']
            parameter67 = serializer.data['parameter67']
            parameter68 = serializer.data['parameter68']
            parameter69 = serializer.data['parameter69']
            parameter70 = serializer.data['parameter70']
            parameter71 = serializer.data['parameter71']
            parameter72 = serializer.data['parameter72']
            parameter73 = serializer.data['parameter73']
            parameter74 = serializer.data['parameter74']
            parameter75 = serializer.data['parameter75']
            parameter76 = serializer.data['parameter76']
            parameter77 = serializer.data['parameter77']
            parameter78 = serializer.data['parameter78']
            parameter79 = serializer.data['parameter79']
            parameter80 = serializer.data['parameter80']
            parameter81 = serializer.data['parameter81']
            parameter82 = serializer.data['parameter82']
            parameter83 = serializer.data['parameter83']
            parameter84 = serializer.data['parameter84']
            parameter85 = serializer.data['parameter85']
            parameter86 = serializer.data['parameter86']
            parameter87 = serializer.data['parameter87']
            parameter88 = serializer.data['parameter88']
            parameter89 = serializer.data['parameter89']
            parameter90 = serializer.data['parameter90']
            parameter91 = serializer.data['parameter91']
            parameter92 = serializer.data['parameter92']
            parameter93 = serializer.data['parameter93']
            parameter94 = serializer.data['parameter94']
            parameter95 = serializer.data['parameter95']
            parameter96 = serializer.data['parameter96']
            parameter97 = serializer.data['parameter97']
            parameter98 = serializer.data['parameter98']
            parameter99 = serializer.data['parameter99']
            parameter100 = serializer.data['parameter100']
            parameter101 = serializer.data['parameter101']
            parameter102 = serializer.data['parameter102']
            parameter103 = serializer.data['parameter103']
            parameter104 = serializer.data['parameter104']
            parameter105 = serializer.data['parameter105']
            parameter106 = serializer.data['parameter106']
            parameter107 = serializer.data['parameter107']
            parameter108 = serializer.data['parameter108']
            parameter109 = serializer.data['parameter109']
            parameter110 = serializer.data['parameter110']
            parameter111 = serializer.data['parameter111']
            parameter112 = serializer.data['parameter112']
            parameter113 = serializer.data['parameter113']
            parameter114 = serializer.data['parameter114']
            parameter115 = serializer.data['parameter115']
            parameter116 = serializer.data['parameter116']
            parameter117 = serializer.data['parameter117']
            parameter118 = serializer.data['parameter118']
            parameter119 = serializer.data['parameter119']
            parameter120 = serializer.data['parameter120']
            parameter121 = serializer.data['parameter121']
            parameter122 = serializer.data['parameter122']
            parameter123 = serializer.data['parameter123']
            parameter124 = serializer.data['parameter124']
            parameter125 = serializer.data['parameter125']
            parameter126 = serializer.data['parameter126']
            parameter127 = serializer.data['parameter127']
            parameter128 = serializer.data['parameter128']
            parameter129 = serializer.data['parameter129']
            parameter130 = serializer.data['parameter130']
            parameter131 = serializer.data['parameter131']
            parameter132 = serializer.data['parameter132']
            parameter133 = serializer.data['parameter133']
            parameter134 = serializer.data['parameter134']
            parameter135 = serializer.data['parameter135']
            parameter136 = serializer.data['parameter136']
            parameter137 = serializer.data['parameter137']
            parameter138 = serializer.data['parameter138']
            parameter139 = serializer.data['parameter139']
            parameter140 = serializer.data['parameter140']
            parameter141 = serializer.data['parameter141']
            parameter142 = serializer.data['parameter142']
            parameter143 = serializer.data['parameter143']
            parameter144 = serializer.data['parameter144']
            parameter145 = serializer.data['parameter145']
            parameter146 = serializer.data['parameter146']
            parameter147 = serializer.data['parameter147']
            parameter148 = serializer.data['parameter148']
            parameter149 = serializer.data['parameter149']
            parameter150 = serializer.data['parameter150']
            parameter151 = serializer.data['parameter151']
            parameter152 = serializer.data['parameter152']
            parameter153 = serializer.data['parameter153']
            parameter154 = serializer.data['parameter154']
            parameter155 = serializer.data['parameter155']
            parameter156 = serializer.data['parameter156']
            parameter157 = serializer.data['parameter157']
            parameter158 = serializer.data['parameter158']
            parameter159 = serializer.data['parameter159']
            parameter160 = serializer.data['parameter160']
            parameter161 = serializer.data['parameter161']
            parameter162 = serializer.data['parameter162']
            parameter163 = serializer.data['parameter163']
            parameter164 = serializer.data['parameter164']
            parameter165 = serializer.data['parameter165']
            parameter166 = serializer.data['parameter166']
            parameter167 = serializer.data['parameter167']
            parameter168 = serializer.data['parameter168']
            parameter169 = serializer.data['parameter169']
            parameter170 = serializer.data['parameter170']
            parameter171 = serializer.data['parameter171']
            parameter172 = serializer.data['parameter172']
            parameter173 = serializer.data['parameter173']
            parameter174 = serializer.data['parameter174']
            parameter175 = serializer.data['parameter175']
            parameter176 = serializer.data['parameter176']
            parameter177 = serializer.data['parameter177']
            parameter178 = serializer.data['parameter178']
            parameter179 = serializer.data['parameter179']
            parameter180 = serializer.data['parameter180']
            parameter181 = serializer.data['parameter181']
            parameter182 = serializer.data['parameter182']
            parameter183 = serializer.data['parameter183']
            parameter184 = serializer.data['parameter184']
            parameter185 = serializer.data['parameter185']
            parameter186 = serializer.data['parameter186']
            parameter187 = serializer.data['parameter187']
            parameter188 = serializer.data['parameter188']
            parameter189 = serializer.data['parameter189']
            parameter190 = serializer.data['parameter190']
            parameter191 = serializer.data['parameter191']
            parameter192 = serializer.data['parameter192']
            parameter193 = serializer.data['parameter193']
            parameter194 = serializer.data['parameter194']
            parameter195 = serializer.data['parameter195']
            parameter196 = serializer.data['parameter196']
            parameter197 = serializer.data['parameter197']
            parameter198 = serializer.data['parameter198']
            parameter199 = serializer.data['parameter199']
            parameter200 = serializer.data['parameter200']
            parameter201 = serializer.data['parameter201']
            parameter202 = serializer.data['parameter202']
            parameter203 = serializer.data['parameter203']
            parameter204 = serializer.data['parameter204']
            parameter205 = serializer.data['parameter205']
            parameter206 = serializer.data['parameter206']
            parameter207 = serializer.data['parameter207']
            parameter208 = serializer.data['parameter208']
            parameter209 = serializer.data['parameter209']
            parameter210 = serializer.data['parameter210']
            parameter211 = serializer.data['parameter211']
            parameter212 = serializer.data['parameter212']
            parameter213 = serializer.data['parameter213']
            parameter214 = serializer.data['parameter214']
            parameter215 = serializer.data['parameter215']
            parameter216 = serializer.data['parameter216']
            parameter217 = serializer.data['parameter217']
            parameter218 = serializer.data['parameter218']
            parameter219 = serializer.data['parameter219']
            parameter220 = serializer.data['parameter220']
            parameter221 = serializer.data['parameter221']
            parameter222 = serializer.data['parameter222']
            parameter223 = serializer.data['parameter223']
            parameter224 = serializer.data['parameter224']
            parameter225 = serializer.data['parameter225']
            parameter226 = serializer.data['parameter226']
            parameter227 = serializer.data['parameter227']
            parameter228 = serializer.data['parameter228']
            parameter229 = serializer.data['parameter229']
            parameter230 = serializer.data['parameter230']
            parameter231 = serializer.data['parameter231']
            parameter232 = serializer.data['parameter232']
            parameter233 = serializer.data['parameter233']
            parameter234 = serializer.data['parameter234']
            parameter235 = serializer.data['parameter235']
            parameter236 = serializer.data['parameter236']
            parameter237 = serializer.data['parameter237']
            parameter238 = serializer.data['parameter238']
            parameter239 = serializer.data['parameter239']
            parameter240 = serializer.data['parameter240']
            parameter241 = serializer.data['parameter241']
            parameter242 = serializer.data['parameter242']
            parameter243 = serializer.data['parameter243']
            parameter244 = serializer.data['parameter244']
            parameter245 = serializer.data['parameter245']
            parameter246 = serializer.data['parameter246']
            parameter247 = serializer.data['parameter247']
            parameter248 = serializer.data['parameter248']
            parameter249 = serializer.data['parameter249']
            parameter250 = serializer.data['parameter250']
            parameter251 = serializer.data['parameter251']
            parameter252 = serializer.data['parameter252']
            parameter253 = serializer.data['parameter253']
            parameter254 = serializer.data['parameter254']
            parameter255 = serializer.data['parameter255']
            parameter256 = serializer.data['parameter256']
            parameter257 = serializer.data['parameter257']
            parameter258 = serializer.data['parameter258']
            parameter259 = serializer.data['parameter259']
            parameter260 = serializer.data['parameter260']
            parameter261 = serializer.data['parameter261']
            parameter262 = serializer.data['parameter262']
            parameter263 = serializer.data['parameter263']
            parameter264 = serializer.data['parameter264']
            parameter265 = serializer.data['parameter265']
            parameter266 = serializer.data['parameter266']
            parameter267 = serializer.data['parameter267']
            parameter268 = serializer.data['parameter268']
            parameter269 = serializer.data['parameter269']
            parameter270 = serializer.data['parameter270']
            parameter271 = serializer.data['parameter271']
            parameter272 = serializer.data['parameter272']
            parameter273 = serializer.data['parameter273']
            parameter274 = serializer.data['parameter274']
            parameter275 = serializer.data['parameter275']
            parameter276 = serializer.data['parameter276']
            parameter277 = serializer.data['parameter277']
            parameter278 = serializer.data['parameter278']
            parameter279 = serializer.data['parameter279']
            parameter280 = serializer.data['parameter280']
            parameter281 = serializer.data['parameter281']
            parameter282 = serializer.data['parameter282']
            parameter283 = serializer.data['parameter283']
            parameter284 = serializer.data['parameter284']
            parameter285 = serializer.data['parameter285']
            parameter286 = serializer.data['parameter286']
            parameter287 = serializer.data['parameter287']
            parameter288 = serializer.data['parameter288']
            parameter289 = serializer.data['parameter289']
            parameter290 = serializer.data['parameter290']
            parameter291 = serializer.data['parameter291']
            parameter292 = serializer.data['parameter292']
            parameter293 = serializer.data['parameter106']
            parameter294 = serializer.data['parameter293']
            parameter295 = serializer.data['parameter295']
            parameter296 = serializer.data['parameter296']
            parameter297 = serializer.data['parameter298']
            parameter298 = serializer.data['parameter298']
            parameter299 = serializer.data['parameter299']
            parameter300 = serializer.data['parameter300']
            parameter301 = serializer.data['parameter301']
            parameter302 = serializer.data['parameter302']
            parameter303 = serializer.data['parameter303']
            parameter304 = serializer.data['parameter304']
            parameter305 = serializer.data['parameter305']
            parameter306 = serializer.data['parameter306']
            parameter307 = serializer.data['parameter307']
            parameter308 = serializer.data['parameter308']
            parameter309 = serializer.data['parameter309']
            parameter310 = serializer.data['parameter310']
            parameter311 = serializer.data['parameter311']
            parameter312 = serializer.data['parameter312']
            parameter313 = serializer.data['parameter313']
            parameter314 = serializer.data['parameter314']
            parameter315 = serializer.data['parameter315']

            try:
                new_record = devices(owner=creator , ID_of_device = ID_of_device , labeled=labeled,
                parameter1= parameter1,
                parameter2 = parameter2,
                parameter3 = parameter3,
                parameter4 = parameter4,
                parameter5 = parameter5,
                parameter6 = parameter6,
                parameter7 = parameter7,
                parameter8 = parameter8,
                parameter9 = parameter9,
                parameter10 = parameter10,
                parameter11 = parameter11,
                parameter12 = parameter12,
                parameter13 = parameter13,
                parameter14 = parameter14,
                parameter15 = parameter15,
                parameter16 = parameter16,
                parameter17 = parameter17,
                parameter18 = parameter18,
                parameter19 = parameter19,
                parameter20 = parameter20,
                parameter21 = parameter21,
                parameter22 = parameter22,
                parameter23 = parameter23,
                parameter24 = parameter24,
                parameter25 = parameter25,
                parameter26 = parameter26,
                parameter27 = parameter27,
                parameter28 = parameter28,
                parameter29 = parameter29,
                parameter30 = parameter30,
                parameter31 = parameter31,
                parameter32 = parameter32,
                parameter33 = parameter33,
                parameter34 = parameter34,
                parameter35 = parameter35,
                parameter36 = parameter36,
                parameter37 = parameter37,
                parameter38 = parameter38,
                parameter39 = parameter39,
                parameter40 = parameter40,
                parameter41 = parameter41,
                parameter42 = parameter42,
                parameter43 = parameter43,
                parameter44 = parameter44,
                parameter45 = parameter45,
                parameter46 = parameter46,
                parameter47 = parameter47,
                parameter48 = parameter48,
                parameter49 = parameter49,
                parameter50 = parameter50,
                parameter51 = parameter51,
                parameter52 = parameter52,
                parameter53 = parameter53,
                parameter54 = parameter54,
                parameter55 = parameter55,
                parameter56 = parameter56,
                parameter57 = parameter57,
                parameter58 = parameter58,
                parameter59 = parameter59,
                parameter60 = parameter60,
                parameter61 = parameter61,
                parameter62 = parameter62,
                parameter63 = parameter63,
                parameter64 = parameter64,
                parameter65 = parameter65,
                parameter66 = parameter66,
                parameter67 = parameter67,
                parameter68 = parameter68,
                parameter69 = parameter69,
                parameter70 = parameter70,
                parameter71 = parameter71,
                parameter72 = parameter72,
                parameter73 = parameter73,
                parameter74 = parameter74,
                parameter75 = parameter75,
                parameter76 = parameter76,
                parameter77 = parameter77,
                parameter78 = parameter78,
                parameter79 = parameter79,
                parameter80 = parameter80,
                parameter81 = parameter81,
                parameter82 = parameter82,
                parameter83 = parameter83,
                parameter84 = parameter84,
                parameter85 = parameter85,
                parameter86 = parameter86,
                parameter87 = parameter87,
                parameter88 = parameter88,
                parameter89 = parameter89,
                parameter90 = parameter90,
                parameter91 = parameter91,
                parameter92 = parameter92,
                parameter93 = parameter93,
                parameter94 = parameter94,
                parameter95 = parameter95,
                parameter96 = parameter96,
                parameter97 = parameter97,
                parameter98 = parameter98,
                parameter99 = parameter99,
                parameter100 = parameter100,
                parameter101 = parameter101,
                parameter102 = parameter102,
                parameter103 = parameter103,
                parameter104 = parameter104,
                parameter105 = parameter105,
                parameter106 = parameter106,
                parameter107 = parameter107,
                parameter108 = parameter108,
                parameter109 = parameter109,
                parameter110 = parameter110,
                parameter111 = parameter111,
                parameter112 = parameter112,
                parameter113 = parameter113,
                parameter114 = parameter114,
                parameter115 = parameter115,
                parameter116 = parameter116,
                parameter117 = parameter117,
                parameter118 = parameter118,
                parameter119 = parameter119,
                parameter120 = parameter120,
                parameter121 = parameter121,
                parameter122 = parameter122,
                parameter123 = parameter123,
                parameter124 = parameter124,
                parameter125 = parameter125,
                parameter126 = parameter126,
                parameter127 = parameter127,
                parameter128 = parameter128,
                parameter129 = parameter129,
                parameter130 = parameter130,
                parameter131 = parameter131,
                parameter132 = parameter132,
                parameter133 = parameter133,
                parameter134 = parameter134,
                parameter135 = parameter135,
                parameter136 = parameter136,
                parameter137 = parameter137,
                parameter138 = parameter138,
                parameter139 = parameter139,
                parameter140 = parameter140,
                parameter141 = parameter141,
                parameter142 = parameter142,
                parameter143 = parameter143,
                parameter144 = parameter144,
                parameter145 = parameter145,
                parameter146 = parameter146,
                parameter147 = parameter147,
                parameter148 = parameter148,
                parameter149 = parameter149,
                parameter150 = parameter150,
                parameter151 = parameter151,
                parameter152 = parameter152,
                parameter153 = parameter153,
                parameter154 = parameter154,
                parameter155 = parameter155,
                parameter156 = parameter156,
                parameter157 = parameter157,
                parameter158 = parameter158,
                parameter159 = parameter159,
                parameter160 = parameter160,
                parameter161 = parameter161,
                parameter162 = parameter162,
                parameter163 = parameter163,
                parameter164 = parameter164,
                parameter165 = parameter165,
                parameter166 = parameter166,
                parameter167 = parameter167,
                parameter168 = parameter168,
                parameter169 = parameter169,
                parameter170 = parameter170,
                parameter171 = parameter171,
                parameter172 = parameter172,
                parameter173 = parameter173,
                parameter174 = parameter174,
                parameter175 = parameter175,
                parameter176 = parameter176,
                parameter177 = parameter177,
                parameter178 = parameter178,
                parameter179 = parameter179,
                parameter180 = parameter180,
                parameter181 = parameter181,
                parameter182 = parameter182,
                parameter183 = parameter183,
                parameter184 = parameter184,
                parameter185 = parameter185,
                parameter186 = parameter186,
                parameter187 = parameter187,
                parameter188 = parameter188,
                parameter189 = parameter189,
                parameter190 = parameter190,
                parameter191 = parameter191,
                parameter192 = parameter192,
                parameter193 = parameter193,
                parameter194 = parameter194,
                parameter195 = parameter195,
                parameter196 = parameter196,
                parameter197 = parameter197,
                parameter198 = parameter198,
                parameter199 = parameter199,
                parameter200 = parameter200,
                parameter201 = parameter201,
                parameter202 = parameter202,
                parameter203 = parameter203,
                parameter204 = parameter204,
                parameter205 = parameter205,
                parameter206 = parameter206,
                parameter207 = parameter207,
                parameter208 = parameter208,
                parameter209 = parameter209,
                parameter210 = parameter210,
                parameter211 = parameter211,
                parameter212 = parameter212,
                parameter213 = parameter213,
                parameter214 = parameter214,
                parameter215 = parameter215,
                parameter216 = parameter216,
                parameter217 = parameter217,
                parameter218 = parameter218,
                parameter219 = parameter219,
                parameter220 = parameter220,
                parameter221 = parameter221,
                parameter222 = parameter222,
                parameter223 = parameter223,
                parameter224 = parameter224,
                parameter225 = parameter225,
                parameter226 = parameter226,
                parameter227 = parameter227,
                parameter228 = parameter228,
                parameter229 = parameter229,
                parameter230 = parameter230,
                parameter231 = parameter231,
                parameter232 = parameter232,
                parameter233 = parameter233,
                parameter234 = parameter234,
                parameter235 = parameter235,
                parameter236 = parameter236,
                parameter237 = parameter237,
                parameter238 = parameter238,
                parameter239 = parameter239,
                parameter240 = parameter240,
                parameter241 = parameter241,
                parameter242 = parameter242,
                parameter243 = parameter243,
                parameter244 = parameter244,
                parameter245 = parameter245,
                parameter246 = parameter246,
                parameter247 = parameter247,
                parameter248 = parameter248,
                parameter249 = parameter249,
                parameter250 = parameter250,
                parameter251 = parameter251,
                parameter252 = parameter252,
                parameter253 = parameter253,
                parameter254 = parameter254,
                parameter255 = parameter255,
                parameter256 = parameter256,
                parameter257 = parameter257,
                parameter258 = parameter258,
                parameter259 = parameter259,
                parameter260 = parameter260,
                parameter261 = parameter261,
                parameter262 = parameter262,
                parameter263 = parameter263,
                parameter264 = parameter264,
                parameter265 = parameter265,
                parameter266 = parameter266,
                parameter267 = parameter267,
                parameter268 = parameter268,
                parameter269 = parameter269,
                parameter270 = parameter270,
                parameter271 = parameter271,
                parameter272 = parameter272,
                parameter273 = parameter273,
                parameter274 = parameter274,
                parameter275 = parameter275,
                parameter276 = parameter276,
                parameter277 = parameter277,
                parameter278 = parameter278,
                parameter279 = parameter279,
                parameter280 = parameter280,
                parameter281 = parameter281,
                parameter282 = parameter282,
                parameter283 = parameter283,
                parameter284 = parameter284,
                parameter285 = parameter285,
                parameter286 = parameter286,
                parameter287 = parameter287,
                parameter288 = parameter288,
                parameter289 = parameter289,
                parameter290 = parameter290,
                parameter291 = parameter291,
                parameter292 = parameter292,
                parameter293 = parameter106,
                parameter294 = parameter293,
                parameter295 = parameter295,
                parameter296 = parameter296,
                parameter297 = parameter298,
                parameter298 = parameter298,
                parameter299 = parameter299,
                parameter300 = parameter300,
                parameter301 = parameter301,
                parameter302 = parameter302,
                parameter303 = parameter303,
                parameter304 = parameter304,
                parameter305 = parameter305,
                parameter306 = parameter306,
                parameter307 = parameter307,
                parameter308 = parameter308,
                parameter309 = parameter309,
                parameter310 = parameter310,
                parameter311 = parameter311,
                parameter312 = parameter312,
                parameter313 = parameter313,
                parameter314 = parameter314,
                parameter315 = parameter315
                )
                new_record.save()
                content = {
                    'detail': 'successfuly added the new record'}
                return Response(content, status=status.HTTP_201_CREATED)
            except:
                content = {'detail': 'Failed to add new record'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class DeviceAPI_View(APIView):
    def get(self, request, format=None, *args, **kwargs):
        records = devices.objects.all()
        seralizer = ViewDevicesRecords_Serializer(records, many=True)

        return Response({"This is a list of all records by device":seralizer.data})

class DeviceFiltered_APIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = View_filteredDevices_serializer

    def get_queryset(self):
        user = self.request.user
        return devices.objects.filter(owner=user)




            
            