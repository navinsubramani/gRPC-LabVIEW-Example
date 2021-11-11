import grpc
from grpc import Channel

#import generated classes
import NoiseWaveformsAndPSDensity_pb2_grpc
import NoiseWaveformsAndPSDensity_pb2

#open a grpc channel
Channel = grpc.insecure_channel('localhost:50060')

#create a client
stub = NoiseWaveformsAndPSDensity_pb2_grpc.SignalGeneratorServiceStub(Channel)

#create a valud request message
Request = NoiseWaveformsAndPSDensity_pb2.noData()
NoiseParam = NoiseWaveformsAndPSDensity_pb2.NoiseParameters()
NoiseParam.sampling_info.number_of_samples = 1000
NoiseParam.sampling_info.sample_rate = 10000
NoiseParam.noiseamplitude = 0.1
NoiseParam.noisetype = 2

#make a call
stub.ApplyNoiseParameters(NoiseParam)
result = stub.GetAnalyzedParameters(Request)

#dislay the result
print ("SINAD : " + str(result.sinad))
print ("THD   : " + str(result.THD_plus_noise))