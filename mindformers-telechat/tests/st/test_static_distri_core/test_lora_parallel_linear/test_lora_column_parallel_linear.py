# Copyright 2024 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Test lora column parallel linear"""
import os
import pytest

base_command = ('msrun --worker_num={device_num} --local_worker_num={device_num} '
                '--master_port=61371 --log_dir=msrun_log --join=True --cluster_time_out=300 '
                'run_lora_column.py --dp {dp} --cp {cp} --tp {tp}')


def build_msrun_command(device_num, dp, cp, tp, skip_weight=False, has_bias=False):
    command = base_command.format(device_num=device_num, dp=dp, cp=cp, tp=tp)
    if skip_weight:
        command += ' --skip_weight'
    if has_bias:
        command += ' --has_bias'
    return command


class TestLoRAColumnParallelLinear:
    """A test class for testing LoRAColumnParallelLinear"""

    @pytest.mark.level1
    @pytest.mark.platform_arm_ascend910b_training
    @pytest.mark.env_onecard
    def test_lora_column_parallel_linear_on_single(self):
        """
        Feature: LoRAColumnParallelLinear
        Description: Test LoRAColumnParallelLinear
        Exception: AssertionError
        """
        sh_path = os.path.split(os.path.realpath(__file__))[0]
        dp, cp, tp = (1, 1, 1)
        ret = os.system(
            f"python {sh_path}/run_lora_column.py --dp {dp} --cp {cp} --tp {tp} --has_bias"
        )
        os.system(f"grep -E 'ERROR|error' {sh_path}/msrun_log/worker_0.log -C 3")
        assert ret == 0

    @pytest.mark.level1
    @pytest.mark.platform_arm_ascend910b_training
    @pytest.mark.env_single
    def test_lora_column_parallel_linear_on_parallel(self):
        """
        Feature: LoRAColumnParallelLinear
        Description: Test LoRAColumnParallelLinear
        Exception: AssertionError
        """
        sh_path = os.path.split(os.path.realpath(__file__))[0]
        device_num = 4
        dp, cp, tp = (2, 2, 1)
        skip_weight = False
        has_bias = True
        ret = os.system(build_msrun_command(device_num, dp, cp, tp, skip_weight, has_bias))
        os.system(f"grep -E 'ERROR|error' {sh_path}/msrun_log/worker_0.log -C 3")
        assert ret == 0
