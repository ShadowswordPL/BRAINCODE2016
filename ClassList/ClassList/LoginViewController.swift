//
//  LoginViewController.swift
//  ClassList
//
//  Created by Tomasz Bąk on 19.03.2016.
//  Copyright © 2016 Za Duzo Tomkow. All rights reserved.
//

import UIKit

class LoginViewController: UIViewController {
    @IBOutlet weak var username: UITextField!
    @IBOutlet weak var password: UITextField!
    @IBOutlet weak var indicator: UIActivityIndicatorView!
    
    override func viewWillAppear(animated: Bool) {
        navigationController?.navigationBarHidden = true
    }
    
    @IBAction func login(sender: UIButton) {
        indicator.startAnimating()
        let delayTime = dispatch_time(DISPATCH_TIME_NOW, Int64(0.5 * Double(NSEC_PER_SEC)))
        dispatch_after(delayTime, dispatch_get_main_queue()) { [weak self] in
            self?.indicator.stopAnimating()
            self?.performSegueWithIdentifier("show classes", sender: nil)
        }
    }
    @IBAction func didTap(sender: UITapGestureRecognizer) {
        view.endEditing(false)
    }
}
