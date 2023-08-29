from ast_models import ASTModel
import torch.nn



sd = torch.load("../src/audioset_10_10_0.4593.pth")

tdim = 100
ast_mdl = ASTModel(input_tdim=tdim)

test_input = torch.rand([10, tdim, 128])
test_output = ast_mdl(test_input)

print(test_output.shape)


tdim = 256
ast_mdl = ASTModel(input_tdim=tdim, label_dim=50, audioset_pretrain=True)

test_input = torch.rand([10, tdim, 128])
test_output = ast_mdl(test_input)

print(test_output.shape)
