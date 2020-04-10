<template>
  <div class="databases-wrapper">

    <b-sidebar
      type="is-light"
      :fullheight="true"
      :fullwidth="false"
      :overlay="false"
      :right="false"
      :open.sync="sidebar_show"
    >
      <div class="p-1 settings-wrapper">
        <div class="settings-title">
          Settings
        </div>
        <b-field label="Search">
          <b-input v-model="search_input"></b-input>
        </b-field>
        <b-checkbox class="settings-checkbox-item" v-model="show_view_table_type">
          Show 'VIEW' table type
        </b-checkbox>
        <br>
        <b-checkbox class="settings-checkbox-item" v-model="show_base_table_type">
          Show 'BASE TABLE' table type
        </b-checkbox>
      </div>
    </b-sidebar>

    <b-button class="settings-button" @click="sidebar_show = !sidebar_show">
      <img src="data:image/svg+xml;utf8;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeD0iMHB4IiB5PSIwcHgiIHZpZXdCb3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA1MTIgNTEyOyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIgd2lkdGg9IjUxMnB4IiBoZWlnaHQ9IjUxMnB4Ij4KPGc+Cgk8Zz4KCQk8Zz4KCQkJPHBhdGggZD0iTTI2Mi43ODUsMzE3LjIwN2MtMS45MTMtNC4wMzItNi43MzYtNS43NTItMTAuNzY5LTMuODM3Yy02LjU2MiwzLjExNC0xMy40NDIsNS42ODgtMjAuNDQ4LDcuNjQ4ICAgICBjLTIuOTMxLDAuODItNS4xNTIsMy4yMTUtNS43NDgsNi4ybC04LjU1Miw0Mi43NThjLTAuODQ0LDQuMjIyLTQuNTgyLDcuMjg3LTguODg4LDcuMjg3aC0yMy4zMjkgICAgIGMtNC4zMDYsMC04LjA0My0zLjA2NC04Ljg4OC03LjI4N2wtOC41NTItNDIuNzU4Yy0wLjU5Ny0yLjk4NS0yLjgxOS01LjM4LTUuNzQ4LTYuMmMtOS44OTgtMi43Ny0xOS40NS02LjcyOC0yOC4zOTEtMTEuNzY0ICAgICBjLTIuNjUzLTEuNDk0LTUuOTItMS4zNzEtOC40NTIsMC4zMTdsLTM2LjI4NiwyNC4xOWMtMy41ODIsMi4zODgtOC4zOTIsMS45MTEtMTEuNDM4LTEuMTMzTDYwLjgsMzE2LjEzMSAgICAgYy0zLjA0NS0zLjA0NS0zLjUyLTcuODU1LTEuMTMzLTExLjQzOGwyNC4xOS0zNi4yODZjMS42ODktMi41MzMsMS44MTItNS43OTksMC4zMTctOC40NTIgICAgIGMtNS4wMzctOC45NDItOC45OTUtMTguNDk1LTExLjc2NC0yOC4zOTFjLTAuODItMi45MzEtMy4yMTUtNS4xNTItNi4yLTUuNzQ4bC00Mi43NTgtOC41NTIgICAgIGMtNC4yMjItMC44NDQtNy4yODctNC41ODItNy4yODctOC44ODh2LTIzLjMyOWMwLTQuMzA2LDMuMDY0LTguMDQzLDcuMjg3LTguODg4bDQyLjc1OC04LjU1MmMyLjk4NS0wLjU5Nyw1LjM4LTIuODE5LDYuMi01Ljc0OCAgICAgYzIuNzctOS44OTgsNi43MjgtMTkuNDUsMTEuNzY0LTI4LjM5MWMxLjQ5NC0yLjY1MiwxLjM3MS01LjkxOS0wLjMxNy04LjQ1Mkw1OS42NjksODguNzM0ICAgICBjLTIuMzg4LTMuNTgzLTEuOTEyLTguMzkyLDEuMTMzLTExLjQzOGwxNi40OTYtMTYuNDk2YzMuMDQ1LTMuMDQ1LDcuODU2LTMuNTIsMTEuNDM4LTEuMTMzbDM2LjI4NiwyNC4xOSAgICAgYzIuNTMyLDEuNjg5LDUuOCwxLjgxMSw4LjQ1MiwwLjMxN2M4Ljk0MS01LjAzNiwxOC40OTMtOC45OTQsMjguMzkxLTExLjc2NGMyLjkzMS0wLjgyLDUuMTUyLTMuMjE1LDUuNzQ4LTYuMmw4LjU1Mi00Mi43NTggICAgIGMwLjg0NC00LjIyMiw0LjU4Mi03LjI4Nyw4Ljg4OC03LjI4N2gyMy4zMjljNC4zMDYsMCw4LjA0MywzLjA2NCw4Ljg4OCw3LjI4N2w4LjU1Miw0Mi43NThjMC41OTcsMi45ODUsMi44MTksNS4zOCw1Ljc0OCw2LjIgICAgIGM5Ljg5OCwyLjc3LDE5LjQ1LDYuNzI4LDI4LjM5MSwxMS43NjRjMi42NTMsMS40OTQsNS45MiwxLjM3MSw4LjQ1Mi0wLjMxN2wzNi4yODYtMjQuMTljMy41ODItMi4zODgsOC4zOTEtMS45MTEsMTEuNDM4LDEuMTMzICAgICBsMTYuNDk2LDE2LjQ5NmMzLjA0NSwzLjA0NSwzLjUyLDcuODU1LDEuMTMzLDExLjQzOGwtMjQuMTksMzYuMjg2Yy0xLjY4OSwyLjUzMy0xLjgxMiw1Ljc5OS0wLjMxNyw4LjQ1MiAgICAgYzUuMDM2LDguOTQxLDguOTk0LDE4LjQ5MywxMS43NjQsMjguMzkxYzAuODIsMi45MzEsMy4yMTUsNS4xNTIsNi4yLDUuNzQ4bDQyLjc1OCw4LjU1MmM0LjIyMiwwLjg0NCw3LjI4Nyw0LjU4Miw3LjI4Nyw4Ljg4OCAgICAgdjIzLjMyOWMwLDQuMzA2LTMuMDY0LDguMDQzLTcuMjg3LDguODg4bC00Mi43NTgsOC41NTJjLTIuOTg1LDAuNTk3LTUuMzgsMi44MTktNi4yLDUuNzVjLTIuMDA5LDcuMTgtNC42NiwxNC4yMjMtNy44OCwyMC45MzQgICAgIGMtMS45MzIsNC4wMjUtMC4yMzQsOC44NTQsMy43OTEsMTAuNzg1YzQuMDI1LDEuOTMzLDguODU1LDAuMjM0LDEwLjc4NS0zLjc5MWMyLjkwNi02LjA1Nyw1LjQwMS0xMi4zNTQsNy40NDItMTguNzc3ICAgICBsMzcuOTkxLTcuNTk4YzExLjc0OS0yLjM1MiwyMC4yNzktMTIuNzU4LDIwLjI3OS0yNC43NDR2LTIzLjMyOWMwLTExLjk4Ni04LjUzLTIyLjM5MS0yMC4yODQtMjQuNzQzbC0zNy45OS03LjU5OCAgICAgYy0yLjQ5Mi03Ljg0NC01LjY1LTE1LjQ3LTkuNDM0LTIyLjc2OWwyMS40OTItMzIuMjM5YzYuNjQ4LTkuOTczLDUuMzIzLTIzLjM2My0zLjE1My0zMS44MzlsLTE2LjQ5Ni0xNi40OTYgICAgIGMtOC40NzctOC40NzYtMjEuODY3LTkuOC0zMS44MzktMy4xNTNsLTMyLjIzOSwyMS40OTJjLTcuMjk5LTMuNzgzLTE0LjkyNS02Ljk0Mi0yMi43NjktOS40MzRsLTcuNTk4LTM3Ljk5ICAgICBDMjMwLjc3Miw4LjUzLDIyMC4zNjYsMCwyMDguMzgsMGgtMjMuMzI5Yy0xMS45ODYsMC0yMi4zOTEsOC41My0yNC43NDMsMjAuMjg0bC03LjU5OCwzNy45OSAgICAgYy03Ljg0NCwyLjQ5Mi0xNS40Nyw1LjY1LTIyLjc2OSw5LjQzNEw5Ny43MDQsNDYuMjE2Yy05Ljk3Mi02LjY0OC0yMy4zNjMtNS4zMjQtMzEuODM5LDMuMTUzTDQ5LjM2OSw2NS44NjUgICAgIGMtOC40NzUsOC40NzYtOS44MDEsMjEuODY1LTMuMTUzLDMxLjgzOWwyMS40OTIsMzIuMjM5Yy0zLjc4Myw3LjI5OS02Ljk0MiwxNC45MjQtOS40MzQsMjIuNzY5bC0zNy45OTEsNy41OTggICAgIEM4LjUzLDE2Mi42NiwwLDE3My4wNjYsMCwxODUuMDUydjIzLjMyOWMwLDExLjk4Niw4LjUzLDIyLjM5MSwyMC4yODQsMjQuNzQzbDM3Ljk5LDcuNTk4YzIuNDkxLDcuODQzLDUuNjUsMTUuNDY5LDkuNDM0LDIyLjc2OSAgICAgTDQ2LjIxNiwyOTUuNzNjLTYuNjQ4LDkuOTczLTUuMzIzLDIzLjM2MywzLjE1MywzMS44MzlsMTYuNDk2LDE2LjQ5NmM4LjQ3Niw4LjQ3NiwyMS44NjYsOS44LDMxLjgzOSwzLjE1M2wzMi4yMzktMjEuNDkyICAgICBjNy4yOTksMy43ODMsMTQuOTI0LDYuOTQyLDIyLjc2OSw5LjQzNGw3LjU5OCwzNy45OTJjMi4zNSwxMS43NSwxMi43NTYsMjAuMjgxLDI0Ljc0MiwyMC4yODFoMjMuMzI5ICAgICBjMTEuOTg2LDAsMjIuMzkxLTguNTMsMjQuNzQzLTIwLjI4NGw3LjU5OC0zNy45OWM2LjIyOS0xLjk3OSwxMi4zNDMtNC4zODYsMTguMjI4LTcuMTggICAgIEMyNjIuOTgzLDMyNi4wNjMsMjY0LjcwMSwzMjEuMjQxLDI2Mi43ODUsMzE3LjIwN3oiIGZpbGw9IiMwMDAwMDAiLz4KCQkJPHBhdGggZD0iTTI2Ni43MzksMjQxLjYzNmMxLjE4LDAuNjA2LDIuNDQsMC44OTMsMy42ODIsMC44OTNjMi45MzYsMCw1Ljc2OS0xLjYwNSw3LjItNC4zOTcgICAgIGM2LjUyLTEyLjcxNSw5Ljk2Ny0yNy4wMzYsOS45NjctNDEuNDE1YzAtNTAuMTA3LTQwLjc2NS05MC44NzMtOTAuODczLTkwLjg3M2MtMjMuODM4LDAtNDYuMzY0LDkuMTYyLTYzLjQzLDI1LjgwMSAgICAgYy0zLjE5NywzLjExNi0zLjI2Miw4LjIzNS0wLjE0NiwxMS40MzFjMy4xMTYsMy4xOTYsOC4yMzQsMy4yNjMsMTEuNDMxLDAuMTQ2YzE0LjAyOS0xMy42NzYsMzIuNTQ3LTIxLjIwOSw1Mi4xNDMtMjEuMjA5ICAgICBjNDEuMTkyLDAsNzQuNzA1LDMzLjUxMiw3NC43MDUsNzQuNzA1YzAsMTEuOTk0LTIuNzU0LDIzLjQ0Ni04LjE4NSwzNC4wMzhDMjYxLjE5NywyMzQuNzI2LDI2Mi43NjYsMjM5LjU5OCwyNjYuNzM5LDI0MS42MzZ6IiBmaWxsPSIjMDAwMDAwIi8+CgkJCTxwYXRoIGQ9Ik0xMjEuMDQzLDE2Mi4xMjVjLTQuMjIzLTEuNDUzLTguODIxLDAuNzkyLTEwLjI3NCw1LjAxNGMtMy4yNjcsOS40OTgtNC45MjQsMTkuNDUtNC45MjQsMjkuNTc3ICAgICBjMCw1MC4xMDgsNDAuNzY2LDkwLjg3Myw5MC44NzMsOTAuODczYzE5LjI3MSwwLDM3LjY4My01Ljk1Niw1My4yNDctMTcuMjI3YzMuNjE2LTIuNjE5LDQuNDI1LTcuNjc0LDEuODA3LTExLjI5ICAgICBjLTIuNjE4LTMuNjE2LTcuNjc0LTQuNDI1LTExLjI5LTEuODA3Yy0xMi43ODgsOS4yNTktMjcuOTIxLDE0LjE1NC00My43NjUsMTQuMTU0Yy00MS4xOTMsMC03NC43MDUtMzMuNTEzLTc0LjcwNS03NC43MDUgICAgIGMwLTguMzM0LDEuMzYtMTYuNTE3LDQuMDQ0LTI0LjMxOEMxMjcuNTA4LDE2OC4xNzUsMTI1LjI2NCwxNjMuNTc2LDEyMS4wNDMsMTYyLjEyNXoiIGZpbGw9IiMwMDAwMDAiLz4KCQkJPHBhdGggZD0iTTQ5Ni40NDIsMzUzLjMxNmwtMjMuMzc3LTQuNjc1Yy0xLjQyNC00LjIzNy0zLjEzOS04LjM3NC01LjEyNy0xMi4zNzNsMTMuMjI2LTE5LjgzOCAgICAgYzUuMDk5LTcuNjUsNC4wODMtMTcuOTItMi40MTgtMjQuNDJsLTEwLjg0LTEwLjg0Yy02LjUwMS02LjUtMTYuNzcxLTcuNTE3LTI0LjQyLTIuNDE4bC0xOS44MzgsMTMuMjI2ICAgICBjLTMuOTk5LTEuOTg4LTguMTM2LTMuNzAzLTEyLjM3My01LjEyNmwtNC42NzUtMjMuMzc3Yy0xLjgwMy05LjAxNS05Ljc4NC0xNS41NTgtMTguOTc3LTE1LjU1OGgtMTUuMzMxICAgICBjLTkuMTkyLDAtMTcuMTc0LDYuNTQzLTE4Ljk3NywxNS41NThsLTQuNjc1LDIzLjM3N2MtNC4yMzcsMS40MjQtOC4zNzQsMy4xMzktMTIuMzczLDUuMTI2bC0xOS44MzgtMTMuMjI2ICAgICBjLTcuNjUtNS4wOTgtMTcuOTItNC4wODMtMjQuNDIsMi40MThsLTEwLjg0LDEwLjg0Yy02LjUwMSw2LjUwMS03LjUxNywxNi43NzEtMi40MTgsMjQuNDJsMTMuMjI2LDE5LjgzOCAgICAgYy0yLjczNCw1LjQ5OC00Ljk0OSwxMS4yNTYtNi42MDUsMTcuMTc3Yy0xLjIwMyw0LjMsMS4zMDgsOC43Niw1LjYwNyw5Ljk2NGM0LjMsMS4yMDMsOC43Ni0xLjMwNyw5Ljk2NC01LjYwNyAgICAgYzEuNzYtNi4yOTIsNC4yNzYtMTIuMzYyLDcuNDc2LTE4LjA0M2MxLjQ5NC0yLjY1MywxLjM3MS01LjkyLTAuMzE3LTguNDUybC0xNS44OTctMjMuODQ1Yy0wLjgzOS0xLjI1OS0wLjY3Mi0yLjk0OSwwLjM5OC00LjAxOSAgICAgbDEwLjg0LTEwLjg0YzEuMDctMS4wNjksMi43Ni0xLjIzNSw0LjAxOS0wLjM5OGwyMy44NDUsMTUuODk3YzIuNTMyLDEuNjg5LDUuNzk5LDEuODExLDguNDUyLDAuMzE3ICAgICBjNS42ODItMy4yLDExLjc1MS01LjcxNiwxOC4wNDMtNy40NzZjMi45MzEtMC44Miw1LjE1Mi0zLjIxNSw1Ljc0OC02LjJsNS42MTktMjguMDk3YzAuMjk2LTEuNDgzLDEuNjEtMi41NiwzLjEyMy0yLjU2aDE1LjMzMSAgICAgYzEuNTEyLDAsMi44MjYsMS4wNzcsMy4xMjMsMi41Nmw1LjYxOSwyOC4wOTljMC41OTcsMi45ODUsMi44MTksNS4zOCw1Ljc0OCw2LjJjNi4yOTIsMS43NiwxMi4zNjIsNC4yNzYsMTguMDQzLDcuNDc2ICAgICBjMi42NTIsMS40OTQsNS45MiwxLjM3MSw4LjQ1Mi0wLjMxN2wyMy44NDUtMTUuODk3YzEuMjU5LTAuODM5LDIuOTQ5LTAuNjczLDQuMDE5LDAuMzk4bDEwLjg0LDEwLjg0ICAgICBjMS4wNjksMS4wNywxLjIzNiwyLjc2LDAuMzk4LDQuMDE5bC0xNS44OTcsMjMuODQ1Yy0xLjY4OSwyLjUzMy0xLjgxMiw1Ljc5OS0wLjMxNyw4LjQ1MmMzLjIsNS42ODIsNS43MTYsMTEuNzUxLDcuNDc2LDE4LjA0MyAgICAgYzAuODIsMi45MzEsMy4yMTUsNS4xNTIsNi4yLDUuNzQ4bDI4LjA5Nyw1LjYxOWMxLjQ4MywwLjI5NiwyLjU2LDEuNjEsMi41NiwzLjEyM3YxNS4zMzFjMCwxLjUxMi0xLjA3NywyLjgyNi0yLjU2LDMuMTIzICAgICBsLTI4LjA5OSw1LjYxOWMtMi45ODUsMC41OTctNS4zOCwyLjgxOS02LjIsNS43NDhjLTEuNzYsNi4yOTItNC4yNzYsMTIuMzYyLTcuNDc2LDE4LjA0M2MtMS40OTQsMi42NTMtMS4zNzEsNS45MiwwLjMxNyw4LjQ1MiAgICAgbDE1Ljg5NywyMy44NDVjMC44MzksMS4yNTksMC42NzIsMi45NDktMC4zOTgsNC4wMTlsLTEwLjg0LDEwLjg0Yy0xLjA2OSwxLjA3LTIuNzU5LDEuMjM2LTQuMDE5LDAuMzk4bC0yMy44NDUtMTUuODk3ICAgICBjLTIuNTMyLTEuNjg4LTUuOC0xLjgxMS04LjQ1Mi0wLjMxN2MtNS42ODIsMy4yLTExLjc1MSw1LjcxNi0xOC4wNDMsNy40NzZjLTIuOTMxLDAuODItNS4xNTIsMy4yMTUtNS43NDgsNi4ybC01LjYxOSwyOC4wOTcgICAgIGMtMC4yOTYsMS40ODMtMS42MSwyLjU2LTMuMTIzLDIuNTZoLTE1LjMzMWMtMS41MTIsMC0yLjgyNi0xLjA3Ny0zLjEyMy0yLjU2bC01LjYxOS0yOC4wOTljLTAuNTk3LTIuOTg1LTIuODE5LTUuMzgtNS43NDgtNi4yICAgICBjLTYuMjkyLTEuNzYtMTIuMzYyLTQuMjc2LTE4LjA0My03LjQ3NmMtMi42NTMtMS40OTQtNS45MjEtMS4zNzEtOC40NTIsMC4zMTdsLTIzLjg0NSwxNS44OTcgICAgIGMtMS4yNTksMC44MzktMi45NDksMC42NzMtNC4wMTktMC4zOThsLTEwLjg0LTEwLjg0Yy0xLjA2OS0xLjA3LTEuMjM2LTIuNzYtMC4zOTgtNC4wMTlsMTUuODk3LTIzLjg0NSAgICAgYzEuNjg5LTIuNTMzLDEuODEyLTUuNzk5LDAuMzE3LTguNDUyYy0zLjItNS42ODItNS43MTYtMTEuNzUxLTcuNDc2LTE4LjA0M2MtMC44Mi0yLjkzMS0zLjIxNS01LjE1Mi02LjItNS43NDhsLTI4LjA5Ny01LjYxOSAgICAgYy0xLjQ4My0wLjI5Ni0yLjU2LTEuNjEtMi41Ni0zLjEyM3YtMTUuMzMxYzAtMS41MTIsMS4wNzctMi44MjYsMi41Ni0zLjEyM2wxLjcyLTAuMzQ0YzQuMzc4LTAuODc2LDcuMjE4LTUuMTM1LDYuMzQxLTkuNTEzICAgICBjLTAuODc2LTQuMzc4LTUuMTMtNy4yMTMtOS41MTQtNi4zNDFsLTEuNzIsMC4zNDRjLTkuMDEzLDEuODA0LTE1LjU1Niw5Ljc4NS0xNS41NTYsMTguOTc4djE1LjMzMSAgICAgYzAsOS4xOTIsNi41NDMsMTcuMTc0LDE1LjU1OCwxOC45NzdsMjMuMzc3LDQuNjc1YzEuNDI0LDQuMjM3LDMuMTM5LDguMzc0LDUuMTI2LDEyLjM3M2wtMTMuMjI2LDE5LjgzOCAgICAgYy01LjEsNy42NS00LjA4MywxNy45MiwyLjQxOCwyNC40MmwxMC44NCwxMC44NGM2LjUwMSw2LjUwMSwxNi43NzEsNy41MTcsMjQuNDIsMi40MThsMTkuODM4LTEzLjIyNiAgICAgYzMuOTk5LDEuOTg4LDguMTM2LDMuNzAzLDEyLjM3Myw1LjEyNmw0LjY3NSwyMy4zNzdDMzU1LjExOSw1MDUuNDU3LDM2My4xLDUxMiwzNzIuMjkzLDUxMmgxNS4zMzEgICAgIGM5LjE5MiwwLDE3LjE3NC02LjU0MywxOC45NzctMTUuNTU4bDQuNjc1LTIzLjM3N2M0LjIzNy0xLjQyNCw4LjM3NC0zLjEzOSwxMi4zNzMtNS4xMjdsMTkuODM4LDEzLjIyNiAgICAgYzcuNjUsNS4wOTksMTcuOTIsNC4wODMsMjQuNDItMi40MThsMTAuODQtMTAuODRjNi41MDEtNi41MDEsNy41MTctMTYuNzcxLDIuNDE4LTI0LjQybC0xMy4yMjYtMTkuODM4ICAgICBjMS45ODgtMy45OTksMy43MDMtOC4xMzYsNS4xMjYtMTIuMzczbDIzLjM3Ny00LjY3NWM5LjAxNC0xLjgwMywxNS41NTctOS43ODQsMTUuNTU3LTE4Ljk3N3YtMTUuMzMxICAgICBDNTEyLDM2My4xLDUwNS40NTcsMzU1LjExOSw0OTYuNDQyLDM1My4zMTZ6IiBmaWxsPSIjMDAwMDAwIi8+CgkJCTxwYXRoIGQ9Ik0zNzkuOTU4LDM1MC44NTVjMTYuMDQ4LDAsMjkuMTAzLDEzLjA1NSwyOS4xMDMsMjkuMTAzYzAsNC40NjUsMy42Miw4LjA4NCw4LjA4NCw4LjA4NHM4LjA4NC0zLjYyLDguMDg0LTguMDg0ICAgICBjMC0yNC45NjMtMjAuMzA5LTQ1LjI3Mi00NS4yNzItNDUuMjcycy00NS4yNzIsMjAuMzA5LTQ1LjI3Miw0NS4yNzJzMjAuMzA5LDQ1LjI3Miw0NS4yNzIsNDUuMjcyICAgICBjMTAuMTExLDAsMTkuNjc1LTMuMjYxLDI3LjY1OS05LjQyOWMzLjUzMy0yLjczLDQuMTg0LTcuODA3LDEuNDU1LTExLjM0MWMtMi43My0zLjUzMy03LjgwOC00LjE4NS0xMS4zNDEtMS40NTUgICAgIGMtNS4xMjgsMy45NjEtMTEuMjc0LDYuMDU2LTE3Ljc3Myw2LjA1NmMtMTYuMDQ4LDAtMjkuMTAzLTEzLjA1NS0yOS4xMDMtMjkuMTAzQzM1MC44NTUsMzYzLjkwOSwzNjMuOTEsMzUwLjg1NSwzNzkuOTU4LDM1MC44NTUgICAgIHoiIGZpbGw9IiMwMDAwMDAiLz4KCQkJPHBhdGggZD0iTTI0NS45NjksMTk2LjcxNmMwLTI3LjE1OC0yMi4wOTYtNDkuMjUzLTQ5LjI1My00OS4yNTNjLTI3LjE1OCwwLTQ5LjI1MywyMi4wOTYtNDkuMjUzLDQ5LjI1MyAgICAgYzAsMjcuMTU4LDIyLjA5NSw0OS4yNTMsNDkuMjUzLDQ5LjI1M1MyNDUuOTY5LDIyMy44NzMsMjQ1Ljk2OSwxOTYuNzE2eiBNMTYzLjYzMSwxOTYuNzE2YzAtMTguMjQyLDE0Ljg0My0zMy4wODUsMzMuMDg1LTMzLjA4NSAgICAgYzE4LjI0MiwwLDMzLjA4NSwxNC44NDMsMzMuMDg1LDMzLjA4NWMwLDE4LjI0Mi0xNC44NDIsMzMuMDg1LTMzLjA4NSwzMy4wODVDMTc4LjQ3MiwyMjkuODAxLDE2My42MzEsMjE0Ljk1OCwxNjMuNjMxLDE5Ni43MTZ6IiBmaWxsPSIjMDAwMDAwIi8+CgkJPC9nPgoJPC9nPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+Cjwvc3ZnPgo=" />
    </b-button>

    <b-table :data="showing_tables" 
      :default-sort-direction="'asc'"
      :sort-icon="'arrow-up'"
      :sort-icon-size="'is-small'"
      default-sort="table_schema"
    >
      <template slot-scope="props">
        <b-table-column field="table_schema" label="Schema" sortable>
          <router-link :to="{ name: 'schema_relations', params: { dbname: $router.currentRoute.params.dbname, dbschema: props.row.table_schema }}">
            {{ props.row.table_schema }}
          </router-link>
        </b-table-column>

        <b-table-column field="table_name" label="Table name" sortable>
          <router-link :to="{ name: 'relation', params: { dbname: $router.currentRoute.params.dbname, dbschema: props.row.table_schema, relation: props.row.table_name }}">
            {{ props.row.table_name }}
          </router-link>
        </b-table-column>

        <b-table-column field="table_type" label="Table type" sortable>
          {{ props.row.table_type }}
        </b-table-column>
      </template>
    </b-table>
  </div>
</template>

<script>

export default {
  name: 'DatabaseRelations',
  data () {
    return {
      tables: [],
      showing_tables: [],
      columns: [
        {
          field: 'table_schema',
          label: 'Schema',
        },
        {
          field: 'table_name',
          label: 'Table name',
        },
        {
          field: 'table_type',
          label: 'Table type',
        },
      ],
      sidebar_show: false,
      show_view_table_type: true,
      show_base_table_type: true,
      search_input: ''
    }
  },
  mounted () {
    this.getDataBaseTables()
  },
  watch: {
    show_base_table_type () {
      this.filterTable()
    },
    show_view_table_type () {
      this.filterTable()
    },
    search_input () {
      this.filterTable()
    }
  },
  methods: {
    getDataBaseTables () {
      this.$http.get(`http://127.0.0.1:5000/databases/${this.$router.currentRoute.params.dbname}/tables`)
      .then(function (response) {
        this.showing_tables = this.tables = response.body
      }.bind(this))
      .catch(function(reject) {
        console.log('Error in getDataBaseTables, reject', reject)
      })
    },
    filterTable () {
      this.showing_tables = this.tables.filter(function(table) {

        if(this.search_input.length > 0) {
          let regex = new RegExp(this.search_input)
          let match_table_name = table.table_name.match(regex)
          let match_table_schema = table.table_schema.match(regex)
          if(match_table_name && match_table_name.length > 0 || match_table_schema && match_table_schema.length > 0) {
            if(this.show_base_table_type && table.table_type === 'BASE TABLE') return true
            else if(this.show_view_table_type && table.table_type === 'VIEW') return true
            else return false
          }
          else {
            return false
          }
        }
        else {
          if(this.show_base_table_type && table.table_type === 'BASE TABLE') return true
          else if(this.show_view_table_type && table.table_type === 'VIEW') return true
          else return false
        }

      }.bind(this))
    }
  }
}
</script>

<style lang="scss">
.databases-wrapper {
  position: relative;

  .settings-button {
    position: fixed;
    right: 0;
    top: 100px;
    padding: 5px;
    width: 50px;
    height: 50px;
    border: 3px solid #7957d5;
    opacity: 0.5;
    transition: opacity .3s;
  }
  .settings-button:hover {
    opacity: 1;
    transition: .3s;
  }
}

.settings-wrapper {
  padding: 10px;

  .settings-title {
    font-size: 16px;
    margin-bottom: 20px;
  }
  .settings-checkbox-item {
    font-size: 14px !important;
    margin-bottom: 12px;
  }
}
</style>