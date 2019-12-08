from django.conf import settings
from django.conf.urls import url, static
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import handler404, handler500

from mygrades.views import (
    student_list_view,
    student_delete_view,
    student_update_view,
    student_setup_view,
    curriculum_create_view,
    curriculum_list_view,
    curriculum_detail_view,
    curriculum_update_view,
    curriculum_delete_view,
    enroll_student_step1,
    enroll_student_step2,
    enroll_delete,
    EnrollmentUpdate,
    weight_edit_view,
    create_weekly_home,
    create_weekly_step1,
    create_weekly_step2,
    report_progress_home,
    report_progress_step1,
    report_progress_step2,
    report_progress_step3,
    report_progress_demo,
    report_card_home,
    report_card_step1,
    report_card_step2,
    report_card_step3,
    report_card_demo,
    see_weekly_home,
    see_weekly_detail,
    see_late_home,
    see_late_detail,
    see_attendance_home,
    see_attendance_detail,
    see_progress_home,
    see_progress_detail,
    see_card_home,
    see_card_detail,
    send_weekly_email,
    send_late_email,
    send_progress_email,
    send_card_email,
    process_gradable_home,
    process_gradable_step1,
    process_gradable_step2,
    crawl,
    standard_create_view,
    standard_list_view,
    standard_update_view,
    standard_delete_view,
    assignment_create_view,
    assignment_list_view,
    assignment_update_view,
    assignment_delete_view,
    student_assignment_list_view,
    grades_record_manual, #new view, keep
    grades_record_manual_edit, #new view, keep
    grades_record_view,
    grades_list_view,
    grades_update_view,
    grades_delete_view,
    student_curriculum_schedule,
    student_curriculum_schedule_detail,
    curriculum_assignment_list,
    standard_upload,
    curriculum_upload,
    assignment_upload,
    teacher_upload,
    student_upload,
    enrollment_upload,
    user_upload,
    send_pacing_guide,
    ShowStudents,
    #StudentAssignmentView,
    user_login,
    user_logout,
    teacher_update_view,
    teacher_delete_view,
    teacher_setup_view,
    teacher_list_view,
    roster_list_view,
    crawler,
    login_help,
    api_curriculum_list,
    tutorials_page_view,
    home_page_view,
    curriculum_assignments_included_view,
    okpromise,
    sat,
    honors,
    drivers_ed,
    work_study,
    act_and_college,
    career_planning,
    concurrent_enrollment,
    prom_graduation,
    military,
    vo_tech,
    email_all_families_view,    
    standards_curriculum_map_view,
    send_plp_email,
    see_plp_home,
    see_plp_detail,
    create_message,
)

urlpatterns = [
    path("create-message/", create_message),
    path("curriculum-map/", standards_curriculum_map_view),
    path("okpromise/",okpromise),
    path("sat/", sat),
    path("honors/",honors),
    path("driver/",drivers_ed),
    path("workstudy/",work_study),
    path("act/",act_and_college),
    path("career/",career_planning),
    path("promgrad/",prom_graduation),
    path("military/",military),
    path("votech/",vo_tech),
    path("concurrent/", concurrent_enrollment),
    path("contact-all/", email_all_families_view),
    path("tutorials/", tutorials_page_view),
    path("login-help/", login_help),
    path("assignment-upload/", assignment_upload, name="assignment_upload"),
    path("curriculum-upload/", curriculum_upload, name="curriculum_upload"),
    path("standard-upload/", standard_upload, name="standard_upload"),
    path("student-upload/", student_upload, name="student_upload"),
    path("enrollment-upload/", enrollment_upload, name="enrollment_upload"),
    path("teacher-upload/", teacher_upload, name="teacher_upload"),
    path("user-upload/", user_upload, name="user_upload"),
    path('myadminscreen/', admin.site.urls),
    path('login/', user_login),
    path('logout/', user_logout),
    path('', home_page_view),
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    # path("api/crawl/", crawl),
    path("students/", student_list_view),
    path("students/<int:epicenter_id>/edit/", student_update_view),
    path("students/<int:epicenter_id>/delete/", student_delete_view),
    path("students-setup/", student_setup_view),
    path("curriculum-schedule/", student_curriculum_schedule),
    path("curriculum-schedule-detail/<int:id>/", student_curriculum_schedule_detail, name="curriculum-schedule-detail"),
    path("curriculum-create/", curriculum_create_view),
    path("curriculum/", curriculum_list_view),
    path("curriculum-update/", curriculum_list_view),
    path("curriculum/<int:id>/", curriculum_detail_view, name="curriculum-detail"),
    path("curriculum/<int:id>/delete/", curriculum_delete_view),
    path("curriculum/<int:id>/edit/", curriculum_update_view),
    path("curriculum-assignments/", curriculum_assignment_list),
    path("enroll-student/", enroll_student_step1, name='enroll_student_step1'),
    path("enroll-student/<str:semester>/<int:student_pk>/", enroll_student_step2, name='enroll_student_step2'),
    path("delete-enrollment/<int:enrollment_pk>/", enroll_delete, name='delete_enrollment'),
    path("edit-entrollment/<int:pk>/", EnrollmentUpdate.as_view(), name='edit_enrollment'),
    path("weight/<str:semester>/<int:student_pk>/<str:subject>/", weight_edit_view, name='weight_edit_view'),
    path("create-weekly-assignment/", create_weekly_home, name="create_weekly_home"),
    path("create-weekly-assignment/<str:semester>/", create_weekly_step1, name="create_weekly_step1"),
    path("create-weekly-assignment/<str:semester>/create/", create_weekly_step2, name="create_weekly_step2"),
    path("report-progress/", report_progress_home, name="report_progress_home"),
    path("report-progress/<str:asem>/", report_progress_step1, name="report_progress_step1"),
    path("report-progress/<str:asem>/create/", report_progress_step2, name="report_progress_step2"),
    path("report-progress/<str:asem>/create/<str:quarter>/<str:sem>/", report_progress_step3, name="report_progress_step3"),
    path("report-progress-demo/<str:student_pk>/<str:asem>/<str:quarter>/<str:sem>/", report_progress_demo, name="report_progress_demo"),
    path("report-card/", report_card_home, name="report_card_home"),
    path("report-card/<str:asem>/", report_card_step1, name="report_card_step1"),
    path("report-card/<str:asem>/create/", report_card_step2, name="report_card_step2"),
    path("report-card/<str:asem>/create/<str:quarter>/<str:sem>/", report_card_step3, name="report_card_step3"),
    path("report-card-demo/<str:student_pk>/<str:asem>/<str:quarter>/<str:sem>/", report_card_demo, name="report_card_demo"),
    path("see-weekly-assignment/", see_weekly_home, name="see_weekly_home"),
    path("see-weekly-assignment/<int:student_pk>/", see_weekly_detail, name="see_weekly_detail"),
    path("see-late-assignment/", see_late_home, name="see_late_home"),
    path("see-late-assignment/<int:student_pk>/", see_late_detail, name="see_late_detail"),
    path("see-report-attendance/", see_attendance_home, name="see_attendance_home"),
    path("see-report-attendance/<int:student_pk>/", see_attendance_detail, name="see_attendance_detail"),
    path("see-report-progress/", see_progress_home, name="see_progress_home"),
    path("see-report-progress/<int:student_pk>/", see_progress_detail, name="see_progress_detail"),
    path("see-report-card/", see_card_home, name="see_card_home"),
    path("see-report-card/<int:student_pk>/", see_card_detail, name="see_card_detail"),
    path("send-weekly-assignment/<int:student_pk>/", send_weekly_email, name="send_weekly_email"),

    path("send-plp/<int:student_pk>/", send_plp_email, name="send_plp_email"),

    path("see-plp/", see_plp_home, name="see_plp_home"),
    path("see-plp/<int:student_pk>/", see_plp_detail, name="see_plp_detail"),
    path("send-late-assignment/<int:student_pk>/", send_late_email, name="send_late_email"),
    path("send-progress/<int:report_pk>/", send_progress_email, name="send_progress_email"),
    path("send-card/<int:report_pk>/", send_card_email, name="send_card_email"),
    path("process-gradable/", process_gradable_home, name="process_gradable"),
    path("process-gradable/choose-week/", process_gradable_step1, name="process_gradable_step1"),
    path("process-gradable/<str:asem>/<int:quarter>/<int:week>/<int:sem>/", process_gradable_step2, name="process_gradable_step2"),
    path("standard-create/", standard_create_view),
    path("standard/", standard_list_view),
    path("standard-update/", standard_list_view),
    path("standard/<int:id>/delete/", standard_delete_view),
    path("standard/<int:id>/edit/", standard_update_view),
    path("assignment-create/", assignment_create_view),
    path("assignment/", assignment_list_view),
    path("assignment-update/", assignment_list_view),
    path("assignment/<int:id>/delete/", assignment_delete_view),
    path("assignment/<int:id>/edit/", assignment_update_view),
    path("assignment/show-students/", ShowStudents.as_view()),
    #path("assignment/student-assignment/<int:id>/", StudentAssignmentView.as_view()),
    path("student-assignment/<int:sid>/<int:cid>/", student_assignment_list_view, name="student-assignment-list-view"),
    path("send-pacing-guide/", send_pacing_guide),
    path("grades-record-manual/<int:enrollment_pk>/", grades_record_manual, name="grades-record-manual"), #new view, keep
    path("grades-record-manual-edit/<int:gradebook_pk>/", grades_record_manual_edit, name="grades-record-manual-edit"), #new view, keep
    path("grades-record/", grades_record_view),
    path("grades/", grades_list_view),
    path("grades-update/", grades_list_view),
    path("grades/<int:id>/delete/", grades_delete_view),
    path("grades/<int:id>/edit/", grades_update_view, name="grades-update-view"),
    url(r'^api/crawl/', crawl, name='crawl'),
    path("teachers/", teacher_list_view),
    path("teachers/<int:id>/edit/", teacher_update_view),
    path("teachers/<int:id>/delete/", teacher_delete_view),
    path("teachers-setup/", teacher_setup_view),
    path("roster/", roster_list_view),
    url(r'^api/crawler/(?P<site_name>.*)/$', crawler, name="crawler"),
    url(r'^api/curriculum/$', api_curriculum_list),

    # path("send-schedule/", ),
    # path("late-assignment/", ),
    # path("progress/", ),
    # path("report-card/", ),
    # path("plp/", ),
]

# This is required for static files while in development mode. (DEBUG=TRUE)
# No, not relevant to scrapy or crawling :)
if settings.DEBUG:
     urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
