#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtx/string_cast.hpp>
#include <iostream>

using namespace std;

int main()
{
	float nx = 100.0f, ny = 50.0f;
	float avp[16] = {
		nx / 2,  0.0f, 0.0f, (nx - 1) / 2,
		 0.0f, ny / 2, 0.0f, (ny - 1) / 2,
		 0.0f,  0.0f, 1.0f,  0.0f,
		 0.0f,  0.0f, 0.0f,  1.0f
	};

	float l = -2.0f, b = 0.0f, n = -3.0f;
	float r = 2.0f, top = 2.0f, f = -6.0f;
	float aorth[16] = {
		2.0 / (r - l), 0.0f, 0.0f,  -(r + l) / (r - l),
		0.0f, 2.0 / (top - b), 0.0f, -(top + b) / (top - b),
		0.0f, 0.0f, 2.0 / (n - f), -(n + f) / (n - f),
		0.0f, 0.0f, 0.0f, 1.0f
	};

	float aper[16] = {
		f, 0, 0, 0,
		0, f, 0, 0,
		0, 0, 0, f * n,
		0, 0, -1, f + n
	};

	float m[16] = {
		-1, 1, -1, 1,
		2, 2, 0, 0,
		-5, -5, -5, -5,
		1, 1, 1, 1
	};

	glm::vec3 e = { 0.0f, 2.0f, 0.0f };
	glm::vec3 g = { 0.0f, -2.0f, -5.0f };
	glm::vec3 t = { 0.0f, 1.0f, 0.0f };

	glm::vec3 w = -(glm::normalize(g));
	glm::vec3 u = glm::normalize(glm::cross(t, w));
	glm::vec3 v = glm::cross(w, u);

	float acam[16] = {
		u.x, v.x, w.x, e.x,
		u.y, v.y, w.y, e.y,
		u.z, v.z, w.z, e.z,
		0, 0, 0, 1
	};

	glm::mat4 mcam = glm::inverse(glm::make_mat4(acam));
	glm::mat4 mvp = glm::transpose(glm::make_mat4(avp));
	glm::mat4 morth = glm::transpose(glm::make_mat4(aorth));
	glm::mat4 mper = glm::transpose(glm::make_mat4(aper));

	glm::mat4 matrix = glm::transpose(glm::make_mat4(m));

	glm::mat4 transform = glm::transpose(((mvp * morth) * mcam) * matrix);

	cout << glm::to_string(mcam) << endl;
	cout << glm::to_string(mper) << endl;
	cout << glm::to_string(transform) << endl;
}
