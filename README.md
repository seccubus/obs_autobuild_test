# obs_autobuild_test
Test to see how you make OpenSUSE build services build automagically with GitHub

Information I based this on
=========================== 
* http://openbuildservice.org/2013/11/22/Source-Update-Via_Token/ - Very sketchy and incomplete
* http://openbuildservice.org/help/manuals/obs-reference-guide/cha.obs.source_service.html - Not very usefull almost internal developer style documentation
* https://en.opensuse.org/openSUSE:Build_Service_Concept_SourceService - Still too high level
* https://en.opensuse.org/openSUSE:Build_Service_private_instance_software_live_cycle - Pretty decent docs. Managed to trigger a build that grabs the software from scm, but then I got stuck
* https://forums.opensuse.org/showthread.php/501869-How-to-define-these-kinds-of-version-format-in-OpenSUSE-Build-Service - Also helpful

Steps I took
============
* Created and empty repo at https://github.com/seccubus/obs_autobuild_test
* Created a new obs package container https://build.opensuse.org/package/show/home:seccubus/obs_autobuild_test
* checked out the obs container
```
$ osc checkout obs_autobuild_test
A    obs_autobuild_test
At revision None.
$
```
* created a new file _service in the obs_autobuild_test directory (see obs/ subdir in github at https://github.com/seccubus/obs_autobuild_test/blob/master/obs/_service)
* checked it in

* created a token
```
 osc token --create home:seccubus obs_autobuild_test
Create a new token
<status code="ok">
  <summary>Ok</summary>
  <data name="token">ReDaCtEdReDaCtEdReDaCtEdReDaCtEd</data>
</status>
```
