# Copyright (c) 2014 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
# -*- coding: utf-8 -*-

from framework.gleantest import GleanTest

# We want to run all tests except those that make problems. The usual problems
# are crash, hangs or running extremely long. A good first guide for removing
# tests is to diff lib64/piglit/tests/quick.py and .../gpu.py.
# TODO(ihf): Figure out how to add tests again.
from tests.all import profile

__all__ = ['profile']

GleanTest.globalParams += ["--quick"]

# These don't test the driver
del profile.tests['glslparsertest']

# These take too long
del profile.tests['glean']['blendFunc']
del profile.tests['glean']['depthStencil']
del profile.tests['glean']['pointAtten']
del profile.tests['spec']['!OpenGL 1.1']['streaming-texture-leak']

# IHF: this test runs with too much memory on my 64 bit dev system
del profile.tests['spec']['!OpenGL 1.2']['tex3d-maxsize']

# IHF: this test hangs testing
del profile.tests['spec']['!OpenGL 1.1']['longprim']
del profile.tests['glx']['glx-make-glxdrawable-current']
del profile.tests['shaders']['glsl-texcoord-array']

# IHF: bug 19813 - x86-generic crashes/hangs blacklisted (roughly declining order of badness)
del profile.tests['spec']['glsl-1.10']['execution']['samplers']['in-parameter']
del profile.tests['spec']['glsl-1.10']['execution']['samplers']['in-parameter-struct']
del profile.tests['spec']['glsl-1.10']['execution']['samplers']['normal-parameter']
del profile.tests['spec']['glsl-1.10']['execution']['samplers']['normal-parameter-struct']

# IHF: This test crashed on lumpy during checkout.
del profile.tests['spec']['!OpenGL 1.1']['max-texture-size']

# IHF: These tests cause hangchecks on lumpy/stumpy and often many crashes and a loss
# of hardware acceleration later. See crosbug.com/30809.
del profile.tests['spec']['glsl-1.30']['execution']['fs-discard-exit-1']
del profile.tests['spec']['glsl-1.30']['execution']['fs-discard-exit-2']

# SCBA: These crashed on Sandy Bridge. Some are not supported.
del profile.tests['spec']['ARB_framebuffer_object']['negative-readpixels-no-rb']
del profile.tests['spec']['ARB_uniform_buffer_object']['maxuniformblocksize/fsexceed']
del profile.tests['spec']['ARB_uniform_buffer_object']['maxuniformblocksize/fs']
del profile.tests['spec']['EGL_KHR_create_context']
del profile.tests['spec']['EGL_NOK_swap_region']
del profile.tests['spec']['EGL_NOK_texture_from_pixmap']
del profile.tests['spec']['EGL 1.4']
del profile.tests['spec']['EXT_texture_array']['compressed teximage']
del profile.tests['spec']['EXT_packed_depth_stencil']['fbo-clear-formats stencil']
del profile.tests['spec']['EXT_texture_compression_s3tc']['s3tc-errors']
del profile.tests['spec']['glsl-1.10']['execution']['varying-packing']
del profile.tests['spec']['glsl-1.30']['execution']['varying-packing-mixed-types']

# SCBA: These crashed on i915
del profile.tests['shaders']['glsl-fs-convolution-2']

# DB: these hang on SNB with HiZ disabled, crbug.com/313085
del profile.tests['spec']['EXT_framebuffer_multisample']
del profile.tests['spec']['!OpenGL 1.1']['copyteximage 2D']
del profile.tests['spec']['ARB_texture_rectangle']['copyteximage RECT']

# IVB: these crash on link.
del profile.tests['shaders']['glsl-fs-inline-explosion']
del profile.tests['shaders']['glsl-vs-inline-explosion']
# These take too long according to quick.py
del profile.tests['shaders']['glsl-fs-unroll-explosion']
del profile.tests['shaders']['glsl-vs-unroll-explosion']

# IVB: these cause GPU hangs on link.
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLod 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLod 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLod 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLod Cube']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLod 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLod 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLod 1DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLod 2DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLod 1DArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLod CubeArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture(bias) 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture(bias) 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture(bias) 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture(bias) Cube']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture(bias) 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture(bias) 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture(bias) CubeShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture(bias) 1DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture(bias) 2DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture(bias) CubeArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture(bias) 1DArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() Cube']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() CubeShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() 1DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() 2DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() CubeArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() 1DArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() 2DArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() 2DRect']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() 2DRectShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection texture() CubeArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset 2DRect']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset 2DRectShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset 1DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset 2DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset 1DArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset 2DArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset(bias) 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset(bias) 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset(bias) 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset(bias) 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset(bias) 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset(bias) 1DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset(bias) 2DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureOffset(bias) 1DArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj 1D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj 2D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj 2DRect']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj 2DRect_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj 2DRectShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj(bias) 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj(bias) 1D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj(bias) 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj(bias) 2D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj(bias) 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj(bias) 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProj(bias) 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset 1D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset 2D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset 2DRect']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset 2DRect_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset 2DRectShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset(bias) 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset(bias) 1D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset(bias) 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset(bias) 2D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset(bias) 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset(bias) 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjOffset(bias) 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLodOffset 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLodOffset 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLodOffset 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLodOffset 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLodOffset 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLodOffset 1DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLodOffset 2DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureLodOffset 1DArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLod 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLod 1D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLod 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLod 2D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLod 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLod 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLod 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLodOffset 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLodOffset 1D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLodOffset 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLodOffset 2D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLodOffset 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLodOffset 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjLodOffset 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad 3D']
#del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad Cube']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad 2DRect']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad 2DRectShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad 2DShadow']
#del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad CubeShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad 1DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad 2DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad 1DArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad 2DArrayShadow']
#del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGrad CubeArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGradOffset 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGradOffset 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGradOffset 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGradOffset 2DRect']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGradOffset 2DRectShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGradOffset 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGradOffset 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGradOffset 1DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGradOffset 2DArray']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGradOffset 1DArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureGradOffset 2DArrayShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGrad 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGrad 1D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGrad 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGrad 2D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGrad 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGrad 2DRect']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGrad 2DRect_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGrad 2DRectShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGrad 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGrad 2DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGradOffset 1D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGradOffset 1D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGradOffset 2D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGradOffset 2D_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGradOffset 2DRect']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGradOffset 2DRect_ProjVec4']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGradOffset 2DRectShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGradOffset 3D']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGradOffset 1DShadow']
del profile.tests['spec']['glsl-1.30']['execution']['tex-miplevel-selection textureProjGradOffset 2DShadow']
