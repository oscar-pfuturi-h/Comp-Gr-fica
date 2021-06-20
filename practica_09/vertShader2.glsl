#version 430
layout (location=0) in vec3 position;

uniform mat4 m_matrix;
uniform mat4 v_matrix;
uniform mat4 proj_matrix;
uniform float tf;

out vec4 varyingColor;

mat4 buildRotateX(float rad); // declaration of matrix transformation utility functions
mat4 buildRotateY(float rad); // (GLSL requires functions to be declared prior to invocation)
mat4 buildRotateZ(float rad);
mat4 buildTranslate(float x, float y, float z);

void main(void)
{ float i = gl_InstanceID + tf; // value based on time factor, but different for each cube instance
float a = sin(2.0 * i) * 8.0; // these are the x, y, and z components for the translation, below
float b = sin(3.0 * i) * 8.0;
float c = sin(4.0 * i) * 8.0;

// build the rotation and translation matrices to be applied to this cube’s model matrix
mat4 localRotX = buildRotateX(10*i);
mat4 localRotY = buildRotateY(10*i);
mat4 localRotZ = buildRotateZ(10*i);
mat4 localTrans = buildTranslate(a,b,c);

// build the model matrix and then the model-view matrix
mat4 newM_matrix = m_matrix * localTrans * localRotX * localRotY * localRotZ;
mat4 mv_matrix = v_matrix * newM_matrix;

gl_Position = proj_matrix * mv_matrix * vec4(position,1.0);
varyingColor = vec4(position,1.0) * 0.5 + vec4(0.5, 0.5, 0.5, 0.5);
}

mat4 buildTranslate(float x, float y, float z)
{ mat4 trans = mat4(1.0, 0.0, 0.0, 0.0,
                    0.0, 1.0, 0.0, 0.0,
		    0.0, 0.0, 1.0, 0.0,
		    x, y, z, 1.0 );
  return trans;
}

mat4 buildRotateX(float rad)
{ mat4 rot = mat4(1.0, 0.0, 0.0, 0.0,
                  0.0, cos(rad), -sin(rad), 0.0,
		  0.0, sin(rad), cos(rad), 0.0,
		  0.0, 0.0, 0.0, 1.0 );
  return rot;
}

mat4 buildRotateY(float rad)
{ mat4 rot = mat4(cos(rad), 0.0, -sin(rad), 0.0,
                  0.0, 1.0, 0.0, 0.0,
		  sin(rad), 0.0, cos(rad), 0.0,
		  0.0, 0.0, 0.0, 1.0 );
  return rot;
}

mat4 buildRotateZ(float rad)
{ mat4 rot = mat4(cos(rad), -sin(rad), 0.0, 0.0,
                  sin(rad), cos(rad), 0.0, 0.0,
		  0.0, 0.0, 1.0, 0.0,
		  0.0, 0.0, 0.0, 1.0 );
  return rot;
}
